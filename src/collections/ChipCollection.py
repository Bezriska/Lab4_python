from src.classes.ChipClass import Chip


class ChipCollection:

    def __init__(self) -> None:
        self.chips = []

    def __iter__(self):
        return iter(self.chips)

    def __len__(self):
        return len(self.chips)

    def __getitem__(self, start=None, end=None, step=None):
        return self.chips[start:end:step]

    def add_chip(self, chip: Chip):
        self.chips.append(chip)


everychip = ChipCollection()

everychip.add_chip(Chip(10))
everychip.add_chip(Chip(25))
everychip.add_chip(Chip(100))


print(everychip.chips[1:2])
