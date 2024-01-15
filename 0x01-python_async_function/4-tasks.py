#!/usr/bin/env python3
"""Asynchronous coroutine"""

import asyncio
from typing import List, Generator

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Iimplementation for the task_wait_n function"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*tasks)
