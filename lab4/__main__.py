"""Demo entry point: run ``python -m lab4``."""

import logging
import sys

from lab4 import (
    ChunkedIterator,
    endless_random,
    log_calls,
    random_numbers,
    sum_numbers,
    take,
)


def _section(title: str) -> None:
    """Print a section header."""
    print()
    print(title)
    print("-" * len(title))


def main() -> None:
    """Print results of every variant task."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s %(name)s: %(message)s",
        stream=sys.stdout,
    )

    _section("Средняя сложность, №7: декоратор логирования")

    @log_calls()
    def add(left: int, right: int) -> int:
        return left + right

    print("add(2, 3) ->", add(2, 3))

    @log_calls()
    def divide(left: float, right: float) -> float:
        return left / right

    try:
        divide(1.0, 0.0)
    except ZeroDivisionError as error:
        print("divide(1.0, 0.0) -> ZeroDivisionError:", error)

    _section("Средняя сложность, №9: случайные числа в диапазоне")
    print(
        "random_numbers(8, 1, 6, seed=42) ->",
        list(random_numbers(8, 1, 6, seed=42)),
    )
    print(
        "повтор с тем же seed совпадает ->",
        list(random_numbers(8, 1, 6, seed=42))
        == list(random_numbers(8, 1, 6, seed=42)),
    )
    print(
        "random_numbers(0, 1, 6) ->",
        list(random_numbers(0, 1, 6)),
    )

    _section("Средняя сложность, №3: сумма через reduce")
    print("sum_numbers([]) ->", sum_numbers([]))
    numbers = [4, 8, 15, 16, 23, 42]
    print("sum_numbers([4, 8, 15, 16, 23, 42]) ->", sum_numbers(numbers))
    print("sum_numbers((1.5, 2, 2.5)) ->", sum_numbers((1.5, 2, 2.5)))

    _section("Повышенная сложность, №7: бесконечный генератор")
    stream = endless_random(1, 6, seed=7)
    print("take(endless_random(1, 6, seed=7), 10) ->", take(stream, 10))
    print(
        "take(endless_random(1, 6, seed=7), 3) ->",
        take(endless_random(1, 6, seed=7), 3),
    )

    _section("Повышенная сложность, №5: собственный итератор")
    print(
        "list(ChunkedIterator(range(1, 8), 3)) ->",
        list(ChunkedIterator(range(1, 8), 3)),
    )
    iterator = ChunkedIterator("abcd", 3)
    print("iter(iterator) is iterator ->", iter(iterator) is iterator)
    print("next(iterator) ->", next(iterator))
    print("next(iterator) ->", next(iterator))


if __name__ == "__main__":
    main()
