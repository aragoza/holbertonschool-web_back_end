#!/usr/bin/env python3


"""
function should return a tuple of size two containing a start
index and an end index corresponding to the range of indexes to
return in a list for those particular pagination parameters
"""


def index_range(page: int, pagesize: int) -> tuple:
    """
    return a tuple with the start index and end index
    """
    starting_index = (page - 1) * pagesize
    ending_index = starting_index + pagesize
    return tuple(starting_index, ending_index)
