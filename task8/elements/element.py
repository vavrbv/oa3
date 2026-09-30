from abc import ABC, abstractmethod


class Element(ABC):
    # Запрос количества очков за удаление элемента с поля.
    # Предусловия: нет.
    @abstractmethod
    def points(self) -> int: ...
