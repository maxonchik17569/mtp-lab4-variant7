"""Tests for the reduce-based sum."""

import unittest

from lab4.sums import sum_numbers


class SumNumbersTests(unittest.TestCase):
    """Checks for :func:`sum_numbers`."""

    def test_empty_iterable_is_zero(self) -> None:
        """An empty input folds to the initial zero."""
        self.assertEqual(sum_numbers([]), 0)

    def test_positive_integers(self) -> None:
        """A list of integers is summed."""
        self.assertEqual(sum_numbers([1, 2, 3, 4]), 10)

    def test_mixed_int_and_float(self) -> None:
        """Floats and integers are summed together."""
        self.assertAlmostEqual(sum_numbers([1, 2.5, -0.5]), 3.0)

    def test_negative_values(self) -> None:
        """Negative numbers are supported."""
        self.assertEqual(sum_numbers([-5, 2, -1]), -4)

    def test_generator_input(self) -> None:
        """Any iterable works, not just sequences."""
        values = (value * 10 for value in range(4))
        self.assertEqual(sum_numbers(values), 60)


if __name__ == "__main__":
    unittest.main()
