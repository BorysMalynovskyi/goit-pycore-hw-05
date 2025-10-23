"""Utilities for extracting and summing income values from text."""
from __future__ import annotations

import re
from collections.abc import Callable, Iterable, Iterator
from math import isclose

NumberGenerator = Iterator[float]


def generator_numbers(text: str) -> NumberGenerator:
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

if __debug__:
    _sample_text = (
        "Загальний дохід працівника складається з декількох частин: 1000.01 "
        "як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 "
        "доларів."
    )
    _expected_numbers = [1000.01, 27.45, 324.0]
    assert list(generator_numbers(_sample_text)) == _expected_numbers
    assert isclose(sum_profit(_sample_text, generator_numbers), 1351.46)
