"""Fibonacci closure with caching."""

from typing import Callable, Dict

from typing import Callable

def caching_fibonacci() -> Callable[[int], int]:
    """Return a Fibonacci function that caches computed values."""

    cache: Dict[int, int] = {0: 0, 1: 1}

    def fibonacci(current_number: int) -> int:
        """Compute the *n*-th Fibonacci number with caching."""

        if current_number in cache:
            return cache[current_number]
        
        if current_number <= 0:
            return 0

        cache[current_number] = fibonacci(current_number - 1) + fibonacci(current_number - 2)
        
        return cache[current_number]

    return fibonacci

if __name__ == "__main__":
    _fibonacci = caching_fibonacci()
    print(_fibonacci(0))
    print(_fibonacci(1))
    print(_fibonacci(5))
    print(_fibonacci(10))
