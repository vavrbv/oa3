from .element import Element


class DefaultElement(Element):
    def points(self) -> int:
        return 10
