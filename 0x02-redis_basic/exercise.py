#!/usr/bin/env python3
"""Redis Basics"""
import redis
import uuid
from typing import Union


class Cache:
    """Cache class"""

    def __init__(self):
        """Constructor method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store method"""
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key
