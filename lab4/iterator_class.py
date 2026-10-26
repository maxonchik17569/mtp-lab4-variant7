"""Own iterator class that splits a sequence into chunks."""

from collections.abc import Iterable, Iterator
from typing import TypeVar

ItemT = TypeVar("ItemT")


class ChunkedIterator(Iterator[tuple[ItemT, ...]]):
    """Iterate over ``items`` in tuples of at most ``size`` elements.

    The source is copied to a tuple, so later changes to a passed
    list do not affect the iteration. The last chunk may be shorter
    than ``size``. The object is its own iterator: ``iter()``
    returns ``self`` and :meth:`__next__` raises
    :class:`StopIteration` once every item is consumed.
    """

    def __init__(self, items: Iterable[ItemT], size: int) -> None:
        """Store the source and validate the chunk size.

        Args:
            items: Any iterable to split into chunks.
            size: Chunk length; must be a positive integer.

        Raises:
            TypeError: If ``size`` is not an integer.
            ValueError: If ``size`` is not positive.
        """
        if not isinstance(size, int):
            raise TypeError(f"size must be an integer, got {size!r}")
        if size <= 0:
            raise ValueError(f"size must be positive, got {size}")
        self._items: tuple[ItemT, ...] = tuple(items)
        self._size = size
        self._index = 0

    def __iter__(self) -> "ChunkedIterator[ItemT]":
        """Return the iterator itself."""
        return self

    def __next__(self) -> tuple[ItemT, ...]:
        """Return the next chunk or raise :class:`StopIteration`."""
        if self._index >= len(self._items):
            raise StopIteration
        stop = self._index + self._size
        chunk = self._items[self._index:stop]
        self._index = stop
        return chunk
