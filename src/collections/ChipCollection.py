from src.classes.ChipClass import Chip


class ChipCollection:
    """Коллекция для управления фишками игрока.
    
    Attributes:
        chips: Список фишек
    """

    def __init__(self) -> None:
        """Инициализирует пустую коллекцию фишек."""

        self.chips = []

    @property
    def summary_value(self):
        """Вычисляет общую стоимость всех фишек"""
        return sum(chip.value for chip in self.chips)

    def __iter__(self):
        """Возвращает итератор по фишкам.
        
        Returns:
            iterator: Итератор по списку фишек
        """
        return iter(self.chips)

    def __len__(self):
        """Возвращает количество фишек в коллекции.
        
        Returns:
            int: Количество фишек
        """
        return len(self.chips)

    def __getitem__(self, start=None, end=None, step=None):
        """Возвращает срез списка фишек.
        
        Args:
            start: Начальный индекс
            end: Конечный индекс
            step: Шаг
            
        Returns:
            list: Список фишек
        """
        return self.chips[start:end:step]

    def __repr__(self):
        """Возвращает строковое представление коллекции фишек.
        
        Returns:
            str: Строка с информацией о фишках и общей стоимости
        """
        return f"ChipCollection(chips={self.chips}, total={self.summary_value})"

    def add_chip(self, chip: Chip):
        """Добавляет фишку в коллекцию.
        
        Args:
            chip: Фишка для добавления
        """
        self.chips.append(chip)

    def add_many_chips(self, chips: list[Chip]):
        """Добавляет несколько фишек в коллекцию.
        
        Args:
            chips: Список фишек для добавления
        """
        for chip in chips:
            self.chips.append(chip)

    def remove_chip(self, value):
        """Удаляет первую фишку с указанным номиналом.
        
        Args:
            value: Номинал фишки для удаления
            
        Raises:
            ValueError: Если фишка с таким номиналом не найдена
        """
        for i, chip in enumerate(self.chips):
            if chip.value == value:
                self.chips.pop(i)
                return
        raise ValueError(f"Chip with value {value} not found")
