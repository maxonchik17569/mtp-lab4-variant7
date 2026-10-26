"""Tests for the custom chunked iterator."""

import unittest

from lab4.iterator_class import ChunkedIterator


class ChunkedIteratorTests(unittest.TestCase):
    """Checks for :class:`ChunkedIterator`."""

    def test_even_chunks(self) -> None:
        """A divisible length gives equal tuple chunks."""
        chunks = list(ChunkedIterator(range(6), 2))
        self.assertEqual(chunks, [(0, 1), (2, 3), (4, 5)])
        self.assertTrue(all(isinstance(chunk, tuple) for chunk in chunks))

    def test_last_chunk_may_be_shorter(self) -> None:
        """The remainder forms a shorter final chunk."""
        chunks = list(ChunkedIterator([1, 2, 3, 4, 5, 6, 7], 3))
        self.assertEqual(chunks, [(1, 2, 3), (4, 5, 6), (7,)])

    def test_is_its_own_iterator(self) -> None:
        """iter() returns self and next() moves forward."""
        iterator = ChunkedIterator("abcd", 3)
        self.assertIs(iter(iterator), iterator)
        self.assertEqual(next(iterator), ("a", "b", "c"))
        self.assertEqual(next(iterator), ("d",))

    def test_exhausted_iterator_stops(self) -> None:
        """StopIteration is raised after the last chunk and stays."""
        iterator = ChunkedIterator([1, 2], 2)
        self.assertEqual(next(iterator), (1, 2))
        with self.assertRaises(StopIteration):
            next(iterator)
        with self.assertRaises(StopIteration):
            next(iterator)

    def test_empty_source_gives_no_chunks(self) -> None:
        """An empty iterable produces no chunks."""
        self.assertEqual(list(ChunkedIterator([], 2)), [])

    def test_source_is_snapshotted(self) -> None:
        """Changing the original list does not affect the iterator."""
        source = [1, 2, 3]
        iterator = ChunkedIterator(source, 2)
        source.append(4)
        self.assertEqual(list(iterator), [(1, 2), (3,)])

    def test_non_positive_size_is_rejected(self) -> None:
        """Zero and negative sizes raise ValueError."""
        for size in (0, -3):
            with self.subTest(size=size):
                with self.assertRaises(ValueError):
                    ChunkedIterator([1, 2, 3], size)

    def test_non_integer_size_is_rejected(self) -> None:
        """A non-integer size raises TypeError."""
        with self.assertRaises(TypeError):
            ChunkedIterator([1, 2, 3], 2.5)


if __name__ == "__main__":
    unittest.main()
