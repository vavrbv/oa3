from abc import ABC, abstractmethod


class Combination(ABC):
    # Запрос на получения количества очков за комбинацию.
    # Предусловия: нет.
    @abstractmethod
    def points(self) -> int: ...
