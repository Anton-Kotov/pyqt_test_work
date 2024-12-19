from random import randint
from typing import List


class GraphPos:
    def __init__(self, x_pos: List[int], y_pos: List[int]):
        self.x_pos = x_pos
        self.y_pos = y_pos


class GraphRandomData:
    """Создает случайные данные для графиков"""

    def __init__(
        self,
        cnt_data: int = 10,
        max_data_size: int = 100,
        max_number: int = 500
    ):
        self.cnt_data = cnt_data
        self.max_data_size = max_data_size
        self.max_number = max_number
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current > self.cnt_data:
            raise StopIteration
        x_pos = sorted(randint(0, self.max_number) for _ in range(self.max_data_size))
        y_pos = sorted(randint(0, self.max_number) for _ in range(self.max_data_size))

        return GraphPos(x_pos, y_pos)

