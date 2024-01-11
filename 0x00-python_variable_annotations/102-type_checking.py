#!/usr/bin/env python3
"""Type Checking Update"""


from typing import Tuple, Union, List, Any


def zoom_array(lst: Tuple, factor: Union[int, float] = 2) -> Tuple:
    """Use mypy to validate the following piece of code
    and apply any necessary changes.
    """	
    zoomed_in: List[Any] = [
        item for item in lst
        for i in range(int(factor))
    ]
    return tuple(zoomed_in)


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
