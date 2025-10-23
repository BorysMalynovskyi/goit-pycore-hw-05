"""Fibonacci closure with caching."""

from typing import Callable, Dict

from typing import Callable

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

if __debug__:
    _fib = caching_fibonacci()
    assert _fib(0) == 0
    assert _fib(1) == 1
    assert _fib(5) == 5
    assert _fib(10) == 55
