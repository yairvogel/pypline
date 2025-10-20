from functools import lru_cache
from typing import Annotated
from pydantic import Field

type PositiveInt = Annotated[int, Field(gt=0)]


@lru_cache
def fib(n: PositiveInt) -> PositiveInt:
    if n == 1 or n == 0:
        return 1
    return fib(n - 1) + fib(n - 2)
