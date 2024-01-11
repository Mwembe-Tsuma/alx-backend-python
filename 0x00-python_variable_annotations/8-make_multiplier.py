#!/usr/bin/env python3
"""Complex types - functions"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float multiplier as an argument and returns a function.
    The returned function multiplies a float by the given multiplier.

    Parameters:
    multiplier (float): The multiplier to be used in the returned function.

    Returns:
    Callable[[float], float]: The returned function that multiplies a float by the given multiplier.
    """
    def multiplier_function(x: float) -> float:
        """Multiplies a float by the given multiplier"""
        return x * multiplier

    return multiplier_function
