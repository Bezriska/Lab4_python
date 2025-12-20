
import pytest

from src.classes.PlayerClass import Player
from src.classes.ChipClass import Chip


class TestPlayer:
    """Тесты для класса Player."""

    def test_player_creation(self):
        """Тестирует создание игрока."""
        player = Player("Иван")
        assert player.name == "Иван"
        assert player.balance == 0
        assert player.dodge_chance == 0.1
        assert player.panic_ind == 0

    def test_player_balance_with_chips(self):
        """Тестирует расчёт баланса игрока с фишками."""
        player = Player("Иван")
        player.chips_col.add_chip(Chip(100))
        player.chips_col.add_chip(Chip(200))
        assert player.balance == 300

    def test_player_repr(self):
        """Тестирует строковое представление игрока."""
        player = Player("Иван")
        player.chips_col.add_chip(Chip(100))
        expected = "Player(name = Иван, balance = 100)"
        assert repr(player) == expected

    def test_make_bet_with_chips(self):
        """Тестирует ставку игрока с фишками."""
        player = Player("Иван")
        player.chips_col.add_chip(Chip(100))
        player.chips_col.add_chip(Chip(200))
        
        initial_count = len(player.chips_col)
        bet_value = player.make_bet()
        
        assert len(player.chips_col) == initial_count - 1
        assert bet_value > 0
        assert bet_value in [100, 200]

    def test_make_bet_without_chips(self):
        """Тестирует ошибку при ставке без фишек."""
        player = Player("Иван")
        with pytest.raises(ValueError):
            player.make_bet()

    def test_dodge_chance_range(self):
        """Тестирует, что шанс уклонения находится в допустимых пределах."""
        player = Player("Иван")
        assert 0 <= player.dodge_chance <= 1

    def test_panic_ind_initial_value(self):
        """Тестирует начальное значение индекса паники."""
        player = Player("Иван")
        assert player.panic_ind == 0