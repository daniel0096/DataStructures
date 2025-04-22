from typing import Any

class AdjacencyError(Exception):
    def __init__(self, err_message: str):
        super().__init__(f'Adjacency list raised an exception: {err_message}')

def require_non_null(function: Any):
    def wrapper(*args, **kwargs):
        for arg in args:
            if arg is None:
                raise AdjacencyError(f'Argument cannot be null.')
        return function(*args, **kwargs)
    return wrapper