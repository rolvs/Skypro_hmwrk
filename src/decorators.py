from __future__ import annotations

from functools import wraps
from typing import Callable, Optional, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def log(filename: Optional[str] = None) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """Логирует успешное выполнение функции или возникшую ошибку."""
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            def write(message: str) -> None:
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(message + "\n")
                else:
                    print(message)

            try:
                result = func(*args, **kwargs)
                write(f"{func.__name__} ok")
                return result
            except Exception as e:
                write(
                    f"{func.__name__} error: {type(e).__name__}. "
                    f"Inputs: {args}, {kwargs}"
                )
                raise

        return wrapper

    return decorator
