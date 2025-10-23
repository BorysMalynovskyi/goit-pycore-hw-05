"""Fibonacci closure with caching.

This module provides the :func:`caching_fibonacci` factory that produces
recursive Fibonacci functions capable of caching previously computed
values. The closure keeps the cache alive between calls to the returned
function.
"""

from typing import Callable, Dict


def caching_fibonacci() -> Callable[[int], int]:
    """Return a Fibonacci function that caches computed values."""

    cache: Dict[int, int] = {0: 0, 1: 1}

    def fibonacci(n: int) -> int:
        """Compute the *n*-th Fibonacci number with caching."""

        if n in cache:
            return cache[n]
        if n <= 0:
            return 0

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci
