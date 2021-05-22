from typing import List, Optional


class Matrix:
    def __init__(self, matrix_string: str):
        matrix: List[List[int]] = []
        for row in matrix_string.split("\n"):
            matrix.append(list(map(lambda s: int(s), row.split(" "))))
        self._matrix = matrix

    def row(self, index: int) -> Optional[List[int]]:
        if index > len(self._matrix):
            raise Exception(f"Invalid row index provided: {index}")
        return self._matrix[index - 1]

    def column(self, index: int) -> Optional[List[int]]:
        if index > len(self._matrix[0]):
            raise Exception(f"Invalid column index provided: {index}")
        return [row[index - 1] for row in self._matrix]
