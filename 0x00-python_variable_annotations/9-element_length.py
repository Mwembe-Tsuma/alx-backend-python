#!/usr/bin/env python3
"""Let's duck type an iterable object"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples.
    Each tuple contains an element from the input list and its length.

    Parameters:
    lst (Iterable[Sequence]): The input iterable of sequences.

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples.
    """
    return [(i, len(i)) for i in lst]
