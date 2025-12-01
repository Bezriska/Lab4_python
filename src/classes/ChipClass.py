from src.classes.STATIC import ALLOWED_CHIPS_VALUES


class Chip:

    def __init__(self, value) -> None:
        if value in ALLOWED_CHIPS_VALUES:
            self.value = value
        else:
            raise ValueError("This value is not allowed")

    def __add__(self, other):
        if isinstance(other, Chip):
            return Chip(self.value + other.value)
        else:
            raise TypeError(f"Can not add Chip and {type(other)}")

    def __repr__(self) -> str:
        return f"Chip({self.value})"
