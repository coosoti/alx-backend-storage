#!/usr/bin/env python3
"""
Building a simple cache
Create a Cache class. In the __init__ method, store an instance of the Redis
 client as a private variable named _redis (using redis.Redis()) and flush the
 instance using flushdb.
Create a store method that takes a data argument and returns a string. The
 method should generate a random key (e.g. using uuid), store the input data
 in Redis using the random key and return the key.
Type-annotate store correctly. Remember that data can be a str, bytes, int
 or float
"""
from typing import Union
import redis
import uuid


class Cache:
    """cache class"""
    def __init__(self) -> None:
        """ Instant of Cache class """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """this method takes data argument and returns a string"""
        key = uuid.uuid4()
        self._redis.set(str(key), data)
        return str(key)
