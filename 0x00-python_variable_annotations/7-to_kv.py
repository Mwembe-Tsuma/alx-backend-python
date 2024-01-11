#!/usr/bin/env python3
""" Complex types - string and int/float to tuple"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string k and an int or float v, returns a tuple.
    The first element is the string k.
    The second element is the square of the int/float v, annotated as a float.

    Parameters:
    k (str): The input string.
    v (Union[int, float]): The input int or float.

    Returns:
    Tuple[str, float]: The tuple with the string k and the square of v.
    """
    return k, float(v ** 2)
