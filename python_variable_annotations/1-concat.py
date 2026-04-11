#!/usr/bin/env python3
"""A type-annotated function add 
that takes a float a and a float b as arguments 
and returns their concatenation as a string."""


def concat(a: float, b: float) -> str:
    """Returns the concatenation of a and b as a string."""
    return str(a) + str(b)
