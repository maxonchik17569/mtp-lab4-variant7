"""Tests for the infinite random stream."""

import unittest

from lab4.infinite_stream import endless_random, take


class EndlessRandomTests(unittest.TestCase):
    """Checks for :func:`endless_random`."""

    def test_stream_keeps_producing_values(self) -> None:
        """The generator never stops and respects the bounds."""
        stream = endless_random(1, 6, seed=5)
        values = [next(stream) for _ in range(100)]
        self.assertEqual(len(values), 100)
        self.assertTrue(all(1 <= value <= 6 for value in values))

    def test_same_seed_gives_same_prefix(self) -> None:
        """Two streams with one seed start identically."""
        first = take(endless_random(0, 100, seed=99), 20)
        second = take(endless_random(0, 100, seed=99), 20)
        self.assertEqual(first, second)

    def test_reversed_bounds_are_rejected(self) -> None:
        """low > high is reported on the first iteration."""
        with self.assertRaises(ValueError):
            take(endless_random(5, 1), 3)


class TakeTests(unittest.TestCase):
    """Checks for :func:`take`."""

    def test_take_cuts_infinite_stream(self) -> None:
        """The helper returns exactly the requested prefix."""
        prefix = take(endless_random(1, 6, seed=3), 15)
        self.assertEqual(len(prefix), 15)
        self.assertTrue(all(1 <= value <= 6 for value in prefix))

    def test_take_stops_at_shorter_iterable(self) -> None:
        """A finite source may be shorter than the limit."""
        self.assertEqual(take([1, 2, 3], 10), [1, 2, 3])

    def test_take_zero_returns_empty_list(self) -> None:
        """Zero count consumes nothing."""
        self.assertEqual(take([1, 2, 3], 0), [])

    def test_take_negative_count_is_rejected(self) -> None:
        """A negative count raises ValueError."""
        with self.assertRaises(ValueError):
            take([1, 2, 3], -1)


if __name__ == "__main__":
    unittest.main()
