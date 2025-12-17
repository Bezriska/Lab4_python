from src.classes.PlayerClass import Player
from src.logger import logger
from src.collections.ChipCollection import ChipCollection


class CasinoBalance:
    """Коллекция для управления игроками и их балансами.
    
    Attributes:
        players: Словарь игроков, где ключ - имя игрока
    """

    def __init__(self) -> None:
        """Инициализирует пустую коллекцию игроков."""

        self.players = {}

    @property
    def summary_balance(self):
        """Вычисляет суммарный баланс всех игроков.
        
        Returns:
            int: Общий баланс всех игроков в коллекции
        """
        return sum(player.balance for player in self.players.values())

    def __iter__(self):
        """Возвращает итератор по именам игроков.
        
        Returns:
            iterator: Итератор по ключам словаря игроков
        """
        return iter(self.players)

    def __len__(self) -> int:
        """Возвращает количество игроков в коллекции.
        
        Returns:
            int: Количество игроков
        """
        return len(self.players)

    def __getitem__(self, name) -> Player:
        """Получает игрока по имени.
        
        Args:
            name: Имя игрока
            
        Returns:
            Player: Объект игрока
            
        Raises:
            KeyError: Если игрок с таким именем не найден
        """
        if name in self.players:
            return self.players[name]
        else:
            raise KeyError(f"Player with name {name} does not found")

    def __setitem__(self, name, balance):
        """Устанавливает новый баланс игроку.
        
        Args:
            name: Имя игрока
            balance: Новый баланс
        """
        bal = self.players[name].balance
        self.players[name].balance = balance
        logger.info(
            f"{name}'s balance has been changed from {bal} to {balance}")

    def add_player(self, player: Player):
        """Добавляет игрока в коллекцию.
        
        Args:
            player: Объект игрока для добавления
        """
        self.players[player.name] = player

    def rm_player(self, name):
        """Удаляет игрока из коллекции.
        
        Args:
            name: Имя игрока для удаления
            
        Raises:
            KeyError: Если игрок с таким именем не найден
        """
        if name in self.players:
            del self.players[name]
        else:
            raise KeyError("Incorrect name")

