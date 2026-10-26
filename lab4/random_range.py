"""Generator of reproducible random integers."""

import random
from collections.abc import Iterator


def random_numbers(
    count: int,
    low: int,
    high: int,
    seed: int | None = None,
) -> Iterator[int]:
    """Yield ``count`` random integers from ``low`` to ``high``.

    Both bounds are inclusive. A dedicated :class:`random.Random`
    instance is created from ``seed``, so two calls with the same
    arguments and seed produce the same sequence without touching
    the global random state. ``seed=None`` keeps the sequence
    unpredictable.

    Args:
        count: Number of values to generate; must be non-negative.
        low: Smallest possible value.
        high: Largest possible value.
        seed: Optional seed for reproducible output.

    Yields:
        Random integers between ``low`` and ``high`` inclusive.

    Raises:
        ValueError: If ``count`` is negative or ``low > high``.
            Because this is a generator function, the check runs
            when iteration starts.
    """
    if count < 0:
        raise ValueError(f"count must be non-negative, got {count}")
    if low > high:
        raise ValueError(f"low must not exceed high: {low} > {high}")
    rng = random.Random(seed)
    for _ in range(count):
        yield rng.randint(low, high)
