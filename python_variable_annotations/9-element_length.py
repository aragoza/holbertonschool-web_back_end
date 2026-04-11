#!/usr/bin/env python3
"""A type-annotated function element_length 
that takes a list of strings lst as argument
and returns a list of tuples, where each tuple contains
the length of the corresponding element in lst and the element itself.
"""


from typing import Sequence, List, Tuple


def element_length(lst: Sequence) -> List[Tuple[str, int]]:
    """Returns a list of tuples, where each tuple contains
    the length of the corresponding element in lst and the element itself."""
    return [(i, len(i)) for i in lst]
