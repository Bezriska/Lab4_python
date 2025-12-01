from src.classes.PlayerClass import Player
from src.logger import logger


class CasinoBalance:

    summary_balance = 0

    def __init__(self) -> None:
        self.players = {}

    def __iter__(self):
        return iter(self.players)

    def __len__(self) -> int:
        return len(self.players)

    def __getitem__(self, name) -> Player:
        if name in self.players:
            return self.players[name]
        else:
            raise KeyError(f"Player with name {name} does not found")

    def __setitem__(self, name, balance):
        bal = self.players[name]

        CasinoBalance.summary_balance -= bal

        self.players[name] = balance
        CasinoBalance.summary_balance += self.players[name]
        logger.info(
            f"{name}'s balance has been changed from {bal} to {self.players[name]}")

    def add_player(self, player: Player):
        self.players[player.name] = player.balance
        CasinoBalance.summary_balance += player.balance


sum_balance = CasinoBalance()
sum_balance.add_player(Player("Alice", 100))
sum_balance.add_player(Player("Petr", 10))
sum_balance["Alice"] = 500

print(sum_balance["Alice"], sum_balance["Petr"])
print(sum_balance.summary_balance)
