from __future__ import annotations

from abc import ABC, abstractmethod


class Coordinate(ABC):
    # Запрос на определение того, что обе координаты находятся рядом.
    # Предусловия: нет.
    @abstractmethod
    def is_near(self, other: Coordinate) -> bool: ...
