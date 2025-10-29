import re
from collections.abc import Callable, Iterable, Iterator
from math import isclose


def generator_numbers(text: str) -> Iterator[float]:
    """Yield every decimal number that is isolated by whitespace in *text*.

    The task guarantees that valid income fragments are written without
    mistakes and separated from surrounding text by whitespace. To honour
    that contract we look for numbers that are not adjacent to any
    non-whitespace characters. The implementation supports integers and
    decimal values using a dot as the separator.
    """
    pattern = re.compile(r"(?<!\S)\d+(?:\.\d+)?(?!\S)")

    for match in pattern.finditer(text):
        yield float(match.group())


def sum_profit(text: str, func: Callable[[str], Iterable[float]]) -> float:
    """Calculate the total income in *text* using the provided generator.

    Parameters
    ----------
    text:
        Source string that potentially contains income fragments.
    func:
        A callable compatible with :func:`generator_numbers` that produces an
        iterable of numeric values extracted from ``text``.
    """
    return sum(func(text))


if __name__ == "__main__":
    _sample_text = (
        "The employee's total income consists of several parts: 1000.01 "
        "as the base income, supplemented by additional receipts of 27.45 "
        "and 324.00 dollars."
    )

    _expected_numbers = [1000.01, 27.45, 324.0]

    print(list(generator_numbers(_sample_text)) == _expected_numbers)

    print(isclose(sum_profit(_sample_text, generator_numbers), 1351.46))
