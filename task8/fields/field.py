from abc import ABC, abstractmethod

from .coordinate import Coordinate


class Field(ABC):
    SWAP_OK = 0
    SWAP_WRONG_COORDINATES = 1
    SWAP_NO_COMBINATION = 2
    SWAP_ERROR = 3

    # Команда перестановки двух элементов игрового поля по координатам.
    # Предусловия: координаты находятся рядом.
    # Постусловия: структура игрового поля изменена, если после перестановки элементов
    # образовалась комбинация. Иначе поле не изменяется.
    @abstractmethod
    def swap(self, coordinate1: Coordinate, coordinate2: Coordinate) -> None: ...

    # Запрос получения результата последней перестановки.
    # Предусловия: нет.
    @abstractmethod
    def get_swap_result(self) -> int: ...

    # Запрос уточнения наличия возможной командации на игровом поле.
    # Комбинация считается возможной, если перестановка двух соседних
    # элементов приводит к её появлению.
    # Предусловия: нет.
    @abstractmethod
    def has_possible_combination(self) -> bool: ...
