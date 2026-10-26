"""Tests for the logging decorator task."""

import logging
import unittest

from lab4.logging_decorator import DEFAULT_LOGGER_NAME, log_calls


class LogCallsTests(unittest.TestCase):
    """Checks for :func:`log_calls`."""

    def test_call_and_result_are_logged(self) -> None:
        """A successful call logs arguments and the returned value."""

        @log_calls()
        def add(left: int, right: int) -> int:
            return left + right

        with self.assertLogs(
            DEFAULT_LOGGER_NAME,
            level="INFO",
        ) as captured:
            self.assertEqual(add(2, 3), 5)

        output = "\n".join(captured.output)
        self.assertIn("call add args=(2, 3) kwargs={}", output)
        self.assertIn("return add -> 5", output)

    def test_keyword_arguments_are_logged(self) -> None:
        """Keyword arguments are reported as a mapping."""

        @log_calls()
        def add(left: int, right: int) -> int:
            return left + right

        with self.assertLogs(
            DEFAULT_LOGGER_NAME,
            level="INFO",
        ) as captured:
            self.assertEqual(add(left=4, right=5), 9)

        output = "\n".join(captured.output)
        self.assertIn("kwargs={'left': 4, 'right': 5}", output)
        self.assertIn("return add -> 9", output)

    def test_custom_logger_is_used(self) -> None:
        """An explicit logger receives the records."""
        custom = logging.getLogger("tests.logging.custom")

        @log_calls(logger=custom)
        def double(value: int) -> int:
            return value * 2

        with self.assertLogs(custom, level="INFO") as captured:
            self.assertEqual(double(21), 42)

        self.assertTrue(
            any("double" in line for line in captured.output),
        )

    def test_error_is_logged_and_reraised(self) -> None:
        """An exception is logged at ERROR level and re-raised."""

        @log_calls()
        def fail(divisor: int) -> float:
            return 1 / divisor

        with self.assertLogs(
            DEFAULT_LOGGER_NAME,
            level="ERROR",
        ) as captured:
            with self.assertRaises(ZeroDivisionError):
                fail(0)

        output = "\n".join(captured.output)
        self.assertIn("error in fail", output)
        self.assertIn("ZeroDivisionError", output)

    def test_metadata_and_value_are_preserved(self) -> None:
        """functools.wraps keeps name, docstring and return value."""

        @log_calls()
        def documented(value: int) -> int:
            """Original docstring."""
            return value * 3

        with self.assertLogs(DEFAULT_LOGGER_NAME, level="INFO"):
            self.assertEqual(documented(4), 12)

        self.assertEqual(documented.__name__, "documented")
        self.assertEqual(documented.__doc__, "Original docstring.")


if __name__ == "__main__":
    unittest.main()
