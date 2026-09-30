from abc import ABC, abstractmethod


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
