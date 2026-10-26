"""Tests for the bounded random number generator."""

import unittest

from lab4.random_range import random_numbers


class RandomNumbersTests(unittest.TestCase):
    """Checks for :func:`random_numbers`."""

    def test_count_and_inclusive_bounds(self) -> None:
        """Every generated value lies inside the closed interval."""
        values = list(random_numbers(200, -3, 3, seed=1))
        self.assertEqual(len(values), 200)
        for value in values:
            self.assertGreaterEqual(value, -3)
            self.assertLessEqual(value, 3)

    def test_single_value_range(self) -> None:
        """Equal bounds always produce that single value."""
        values = list(random_numbers(5, 7, 7, seed=0))
        self.assertEqual(values, [7] * 5)

    def test_seed_makes_sequence_reproducible(self) -> None:
        """The same seed gives the same sequence."""
        first = list(random_numbers(10, 0, 1000, seed=123))
        second = list(random_numbers(10, 0, 1000, seed=123))
        self.assertEqual(first, second)

    def test_different_seeds_differ(self) -> None:
        """Different seeds give different sequences."""
        first = list(random_numbers(10, 0, 1000, seed=1))
        second = list(random_numbers(10, 0, 1000, seed=2))
        self.assertNotEqual(first, second)

    def test_zero_count_is_empty(self) -> None:
        """Zero count yields nothing, even without a seed."""
        self.assertEqual(list(random_numbers(0, 1, 10)), [])

    def test_negative_count_is_rejected(self) -> None:
        """A negative count raises ValueError."""
        with self.assertRaises(ValueError):
            list(random_numbers(-1, 1, 10))

    def test_reversed_bounds_are_rejected(self) -> None:
        """low > high raises ValueError."""
        with self.assertRaises(ValueError):
            list(random_numbers(3, 10, 1))


if __name__ == "__main__":
    unittest.main()
