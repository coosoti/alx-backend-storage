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
from typing import Callable, Counter, Optional, Union
import redis
import sys
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """count number of calls made to a method"""
    key = method.__qualname__

    @wraps(method)
    def counter(self, *args, **kwargs):
        """decorator method"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return counter


class Cache:
    """cache class"""
    def __init__(self) -> None:
        """ Instant of Cache class """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """this method takes data argument and returns a string"""
        key = uuid.uuid4()
        self._redis.set(str(key), data)
        return str(key)

    def get(self, key: str, fn: Optional[Callable] = None) ->\
        Union[str, bytes, int, float]:
        """retieves value from server, convert it to desired format"""
        return fn(self._redis.get(key)) if fn else self._redis.get(key)

    def get_int(self, data_bytes: bytes) -> int:
        """convert data bytes from server back to int"""
        return int.from_bytes(data_bytes, sys.byteorder)

    def get_str(self, data_bytes: bytes) -> str:
        """convert data bytes from server back into str"""
        return data_bytes.decode('utf-8')
