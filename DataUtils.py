from typing import Callable, Any
from functools import wraps

class LinkedListException(Exception):
    def __init__(self, error_message: str):
        super().__init__(f'Runtime error: {error_message}')

def requires_non_empty(function: Callable[[Any], None]):
    @wraps(function)
    def wrapper(*args, **kwargs) -> Any:
        self = args[0]
        if self.is_empty():
            raise LinkedListException('Given operation requires size at least greater than 0.')
        return function(*args, **kwargs)
    return wrapper

def requires_not_null(function: Callable[[Any], None]):
    @wraps(function)
    def wrapper(*args, **kwargs) -> Any:
        for x in args:
            if x is None:
                raise LinkedListException('Argument {x} cannot be null.')
        return function(*args, **kwargs)
    return wrapper