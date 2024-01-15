#!/usr/bin/env python3
"""Asynchronous coroutine"""

import asyncio
from typing import Generator

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Implementation for the task_wait_random function"""
    return asyncio.create_task(wait_random(max_delay))
