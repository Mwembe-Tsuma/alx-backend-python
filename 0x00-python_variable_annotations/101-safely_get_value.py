#!/usr/bin/env python3
""" More involved type annotations"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieves the value associated with the given key.

    Parameters:
    dct (Mapping): The input dictionary.
    key (Any): The key to search for in the dictionary.
    default (Union[T, None]): The default value to return

    Returns:
    Union[Any, T]: The value associated with the key if found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
