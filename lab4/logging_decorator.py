"""Decorator that logs calls of the wrapped function."""

import functools
import logging
from collections.abc import Callable
from typing import TypeVar

ResultT = TypeVar("ResultT")

DEFAULT_LOGGER_NAME = "lab4.calls"


def log_calls(
    logger: logging.Logger | None = None,
) -> Callable[[Callable[..., ResultT]], Callable[..., ResultT]]:
    """Wrap a function so that every call is written to ``logger``.

    The wrapper reports three events at ``INFO`` level: the function
    name together with positional and keyword arguments, and the
    returned result. A failed call is reported at ``ERROR`` level
    with the exception type and message, and then the exception is
    re-raised unchanged, so the decorator never hides errors.
    Metadata of the original function is preserved with
    :func:`functools.wraps`.

    Args:
        logger: Target logger. When omitted, the module logger
            ``logging.getLogger("lab4.calls")`` is used.

    Returns:
        A decorator that wraps a function and returns the wrapper.
    """
    active_logger = (
        logger
        if logger is not None
        else logging.getLogger(DEFAULT_LOGGER_NAME)
    )

    def decorator(func: Callable[..., ResultT]) -> Callable[..., ResultT]:
        @functools.wraps(func)
        def wrapper(*args: object, **kwargs: object) -> ResultT:
            active_logger.info(
                "call %s args=%r kwargs=%r",
                func.__name__,
                args,
                kwargs,
            )
            try:
                result = func(*args, **kwargs)
            except Exception as error:
                active_logger.error(
                    "error in %s: %s: %s",
                    func.__name__,
                    type(error).__name__,
                    error,
                )
                raise
            active_logger.info("return %s -> %r", func.__name__, result)
            return result

        return wrapper

    return decorator
