class Goose:

    def __init__(self) -> None:
        self.name: str | None = None


class WarGoose(Goose):

    def __init__(self) -> None:
        super().__init__()
        self.damage = 10


class HonkGoose(Goose):

    def __init__(self) -> None:
        super().__init__()
        self.honk_volume = 10
