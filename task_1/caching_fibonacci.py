"""Fibonacci closure with caching and a simple console interface."""

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


def interactive_fibonacci_loop() -> None:
    """Interactively prompt the user for Fibonacci numbers to calculate."""

    fib = caching_fibonacci()

    while True:
        user_input = input(
            "Enter a non-negative integer for Fibonacci (or 'exit' to quit): "
        ).strip()

        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        if not user_input:
            print("Please enter a value or type 'exit' to quit.")
            continue

        try:
            number = int(user_input)
        except ValueError:
            print("Input must be an integer. Try again.")
            continue

        if number < 0:
            print("Please enter a non-negative integer.")
            continue

        result = fib(number)
        print(f"Fibonacci({number}) = {result}")


if __name__ == "__main__":
    interactive_fibonacci_loop()


assets = [caching_fibonacci, interactive_fibonacci_loop]
