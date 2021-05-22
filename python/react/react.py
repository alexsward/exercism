from typing import Callable, List, NoReturn


class InputCell:
    def __init__(self, initial_value: int):
        self._value = initial_value
        self._watchers: List[ComputeCell] = []

    @property
    def value(self) -> int:
        return self._value
    
    @value.setter
    def value(self, new_value) -> NoReturn:
        self._value = new_value
        for watcher in self._watchers:
            watcher.recompute()

    def watching(self, watcher) -> NoReturn:
        self._watchers.append(watcher)


class ComputeCell:
    def __init__(self, inputs: List[InputCell], compute_function: Callable[[List[int]], int]):
        self._inputs = inputs
        self._fn: Callable[[List[int]], int] = compute_function
        self._value = self.recompute()
        self._callbacks = set()

    @property
    def value(self) -> int:
        self.recompute()
        return self._value

    def recompute(self) -> None:
        cells: List[int] = [cell.value for cell in self._inputs]
        self._value = self._fn(cells)

    def add_callback(self, callback):
        self._callbacks.add(callback)

    def remove_callback(self, callback):
        if callback in self._callbacks:
            self._callbacks.remove(callback)
