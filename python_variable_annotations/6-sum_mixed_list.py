#!/usr/bin/env python3
"""A type-annotated function sum_mixed_list
which takes a list mxd_lst of integers and
floats and returns their sum as a float"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of all the integers and floats
    in mxd_lst as a float."""
    sum: float = 0.0
    for i in mxd_lst:
        sum += float(i)
    return sum
