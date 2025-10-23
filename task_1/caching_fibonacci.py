"""Fibonacci closure with caching.

This module provides the :func:`caching_fibonacci` factory that produces
recursive Fibonacci functions capable of caching previously computed
values. The closure keeps the cache alive between calls to the returned
function.
"""

from typing import Callable

def caching_fibonacci() -> Callable[[int], int]:
    """Return a Fibonacci function that caches computed values."""

    cache: dict[int, int] = {0: 0, 1: 1}

    def fibonacci(n: int) -> int:
        """Compute the *n*-th Fibonacci number with caching."""

        if n in cache:
            return cache[n]
        if n <= 0:
            return 0

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


def caching_fibonacci_console() -> None:
    fibonacci = caching_fibonacci()

    while True:
        user_input = input("Enter a non-negative integer (blank to exit): ").strip()

        if user_input == "":
            break

        try:
            position = int(user_input)
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if position < 0:
            print("Please enter a non-negative integer.")
            continue

        print(f"Fibonacci({position}) = {fibonacci(position)}")


if __name__ == "__main__":
    caching_fibonacci_console()
