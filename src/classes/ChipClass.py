from src.STATIC import ALLOWED_CHIPS_VALUES


class Chip:
    """Класс, представляющий игровую фишку с определенным номиналом.
    
    Attributes:
        value: Номинал фишки
    """

    def __init__(self, value) -> None:
        """Инициализирует фишку с заданным номиналом.
        
        Args:
            value: Номинал фишки
        """

        self.value = value

    def __add__(self, other):
        """Складывает номиналы двух фишек.
        
        Args:
            other: Другая фишка для сложения
            
        Returns:
            Chip: Новая фишка с суммой номиналов
            
        Raises:
            TypeError: Если other не является фишкой
        """
        if isinstance(other, Chip):
            return Chip(self.value + other.value)
        else:
            raise TypeError(f"Can not add Chip and {type(other)}")

    def __repr__(self) -> str:
        """Возвращает строковое представление фишки.
        
        Returns:
            str: Строковое представление фишки
        """
        return f"Chip({self.value})"
