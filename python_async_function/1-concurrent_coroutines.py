#!/usr/bin/env python3
"""An async routine called wait_n that takes in 2 int
arguments (in this order): n and max_delay. You will
spawn wait_random n times with the specified max_delay.
"""

import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Returns a list of all the delays (float values) of wait_random
    called n times with the specified max_delay.
    """
    delays = []
    for i in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)
    delays = sorted(delays)
    return delays
