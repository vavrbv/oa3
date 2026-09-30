from __future__ import annotations

from abc import ABC, abstractmethod


class Combination(ABC):
    # Запрос на получения количества очков за комбинацию.
    # Предусловия: нет.
    @abstractmethod
    def points(self) -> int: ...


class Element(ABC):
    # Запрос количества очков за удаление элемента с поля.
    # Предусловия: нет.
    @abstractmethod
    def points(self) -> int: ...


class Coordinate(ABC):
    # Запрос на определение того, что обе координаты находятся рядом.
    # Предусловия: нет.
    @abstractmethod
    def is_near(self, other: Coordinate) -> bool: ...


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


class MainLoop(ABC):
    # Команда запуска игры.
    # Предусловия: игра не запущена.
    # Постусловия: игра запущена.
    @abstractmethod
    def start(self) -> None: ...

    # Команда перезапуска игры.
    # Предусловия: игра запущена.
    # Постусловия: игровое поле пересоздано, игра запущена.
    @abstractmethod
    def restart(self) -> None: ...

    # Команда завершения игры.
    # Предусловия: игра запущена.
    # Послусловия: игра завершена.
    @abstractmethod
    def end(self) -> None: ...
