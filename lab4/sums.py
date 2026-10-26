"""Sum of numeric values built on ``functools.reduce``."""

import functools
import operator
from collections.abc import Iterable


def sum_numbers(values: Iterable[int | float]) -> int | float:
    """Return the arithmetic sum of ``values``.

    The sum is folded with ``functools.reduce`` and
    ``operator.add`` starting from ``0``, so an empty iterable
    returns ``0`` instead of raising an error.

    Args:
        values: Any iterable of numbers.

    Returns:
        The sum of all values, or ``0`` for an empty iterable.
    """
    return functools.reduce(operator.add, values, 0)
