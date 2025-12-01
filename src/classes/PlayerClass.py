class Player:

    def __init__(self, name, balance=0) -> None:
        self.balance: int = balance
        self.name = name
        self.dodge_chance = 0.1

    def __repr__(self):
        return f"Player(name = {self.name}, balance = {self.balance})"
