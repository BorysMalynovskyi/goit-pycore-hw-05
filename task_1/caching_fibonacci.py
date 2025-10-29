"""Fibonacci closure with caching."""

from typing import Callable, Dict


def caching_fibonacci() -> Callable[[int], int]:
    """Return a Fibonacci function that caches computed values."""

    cache: Dict[int, int] = {0: 0, 1: 1}

    def fibonacci(number: int) -> int:
        """Compute the *n*-th Fibonacci number with caching."""

        if number in cache:
            return cache[number]

        if number <= 0:
            return 0

        cache[number] = fibonacci(number - 1) + fibonacci(number - 2)

        return cache[number]

    return fibonacci


if __name__ == "__main__":
    _fibonacci = caching_fibonacci()
    print(_fibonacci(0))
    print(_fibonacci(1))
    print(_fibonacci(5))
    print(_fibonacci(10))
