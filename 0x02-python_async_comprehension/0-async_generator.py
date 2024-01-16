#!/usr/bin/env python3
"""Async Generator"""

import asyncio
import random


async def async_generator():
    """Implementation of the async_generator coroutine"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
