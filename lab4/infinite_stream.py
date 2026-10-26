"""Infinite random stream and a safe prefix helper."""

import itertools
import random
from collections.abc import Iterable, Iterator
from typing import TypeVar

ItemT = TypeVar("ItemT")


def endless_random(
    low: int,
    high: int,
    seed: int | None = None,
) -> Iterator[int]:
    """Yield random integers from ``low`` to ``high`` endlessly.

    Both bounds are inclusive. The local :class:`random.Random`
    instance makes the stream reproducible for a fixed ``seed``.
    Since the stream never ends, consumers should bound it, for
    example with :func:`take`.

    Args:
        low: Smallest possible value.
        high: Largest possible value.
        seed: Optional seed for reproducible output.

    Yields:
        Random integers between ``low`` and ``high`` inclusive.

    Raises:
        ValueError: If ``low > high``. Because this is a generator
            function, the check runs when iteration starts.
    """
    if low > high:
        raise ValueError(f"low must not exceed high: {low} > {high}")
    rng = random.Random(seed)
    while True:
        yield rng.randint(low, high)


def take(iterable: Iterable[ItemT], count: int) -> list[ItemT]:
    """Return the first ``count`` items of ``iterable`` as a list.

    The prefix is cut with :func:`itertools.islice`, so infinite
    iterables are supported and the source is never over-read.

    Args:
        iterable: Source of items, possibly infinite.
        count: Maximum number of items to return; must be
            non-negative.

    Returns:
        A list with at most ``count`` items.

    Raises:
        ValueError: If ``count`` is negative.
    """
    if count < 0:
        raise ValueError(f"count must be non-negative, got {count}")
    return list(itertools.islice(iterable, count))
