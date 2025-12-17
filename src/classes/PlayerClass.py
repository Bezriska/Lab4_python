from src.collections.ChipCollection import ChipCollection, Chip
import random


class Player:
    """Класс, представляющий игрока в казино.
    
    Attributes:
        name: Имя игрока
        dodge_chance: Шанс уклонения от атаки гуся
        panic_ind: Индекс паники (в процентах)
        chips_col: Коллекция фишек игрока
    """

    def __init__(self, name: str) -> None:
        """Инициализирует игрока с заданным именем.
        
        Args:
            name: Имя игрока
        """

        self.name = name
        self.dodge_chance = 0.1
        self.panic_ind = 0
        self.chips_col = ChipCollection()

    @property
    def balance(self):
        """Возвращает текущий баланс игрока (сумму всех фишек).
        
        Returns:
            int: Общая стоимость всех фишек игрока
        """
        return self.chips_col.summary_value

    def __repr__(self):
        """Возвращает строковое представление игрока.
        
        Returns:
            str: Строка с именем и балансом игрока
        """
        return f"Player(name = {self.name}, balance = {self.balance})"

    def make_bet(self):
        """Делает ставку случайной фишкой из коллекции игрока.
        
        Returns:
            int: Номинал поставленной фишки
            
        Raises:
            ValueError: Если у игрока нет доступных фишек
        """
        if not self.chips_col.chips:
            raise ValueError("No chips available for betting")
        chip = random.choice(self.chips_col.chips)
        bet_value = chip.value
        self.chips_col.remove_chip(bet_value)
        return bet_value

    def clean_chips(self):
        """Удаляет все фишки игрока."""
        self.chips_col.chips = []

