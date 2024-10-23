from pydantic import BaseModel
from typing import Union


__all__ = ["chen"]


class Data(BaseModel):
    """"""
    def __init__(self, **kwargs):
        """大基数按"""
        super().__init__(**kwargs)

    def chen(self, a: Union[float, int], b: Union[float, int]) -> float:
        """计算两数之和

        Examples:
            >>> add(4.0, 2.0)
            6.0
            >>> add(4, 2)
            6.0

        Args:
            a: A number representing the first addend in the addition.
            b: A number representing the second addend in the addition.

        Returns:
            A number representing the arithmetic sum of `a` and `b`.
        """
        return float(a + b)
