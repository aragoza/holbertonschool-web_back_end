#!/usr/bin/env python3
"""A function async_generator that takes no arguments
and loops 10 times asynchronously, each time wait 1 second, then yield a
random number between 0 and 10. Use the random module."""


import asyncio
import random


async def async_generator():
    """
    Loops 10 times asynchronously, each time wait 1 second, then yield a
    random number between 0 and 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
