#!/usr/bin/env python3

"""
function should return a tuple of size two containing a start
index and an end index corresponding to the range of indexes to
return in a list for those particular pagination parameters
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    return a tuple with the start index and end index
    """
    starting_index = (page - 1) * page_size
    ending_index = starting_index + page_size
    start_end = (starting_index, ending_index)
    return start_end
