import pytest

from src.classes.CasinoClass import Casino
from src.classes.GooseClasess import Goose, WarGoose, HonkGoose


class TestCasino:
    """Тесты для класса Casino."""

    def test_casino_creation(self):
        """Тестирует создание казино."""
        casino = Casino()
        assert casino.summary_players_balance == 0
        assert len(casino.player_collection) == 0
        assert len(casino.goose_collection) == 0

    def test_casino_with_seed(self):
        """Тестирует создание казино с фиксированным сидом."""
        casino = Casino(seed=42)
        assert casino.summary_players_balance == 0

    def test_player_registry_without_balance(self):
        """Тестирует регистрацию игрока без начального баланса."""
        casino = Casino()
        casino.player_registry("Иван")
        
        assert len(casino.player_collection) == 1
        assert "Иван" in casino.player_collection.players
        assert casino.player_collection["Иван"].balance == 0

    def test_player_registry_with_balance(self):
        """Тестирует регистрацию игрока с начальным балансом."""
        casino = Casino()
        casino.player_registry("Мария", 1000)
        
        assert len(casino.player_collection) == 1
        assert "Мария" in casino.player_collection.players
        assert casino.player_collection["Мария"].balance == 1000

    def test_goose_registry_regular(self):
        """Тестирует регистрацию обычного гуся."""
        casino = Casino()
        casino.goose_registry("Goose", "Серый", 100)
        
        assert len(casino.goose_collection) == 1
        assert "Серый" in casino.goose_collection.gooses
        assert isinstance(casino.goose_collection.gooses["Серый"], Goose)
        assert casino.goose_collection.gooses["Серый"].balance == 100

    def test_goose_registry_war(self):
        """Тестирует регистрацию боевого гуся."""
        casino = Casino()
        casino.goose_registry("WarGoose", "Боец", 200)
        
        assert len(casino.goose_collection) == 1
        assert "Боец" in casino.goose_collection.gooses
        assert isinstance(casino.goose_collection.gooses["Боец"], WarGoose)
        assert casino.goose_collection.gooses["Боец"].damage == 10

    def test_goose_registry_honk(self):
        """Тестирует регистрацию кричащего гуся."""
        casino = Casino()
        casino.goose_registry("HonkGoose", "Крикун", 150)
        
        assert len(casino.goose_collection) == 1
        assert "Крикун" in casino.goose_collection.gooses
        assert isinstance(casino.goose_collection.gooses["Крикун"], HonkGoose)
        assert casino.goose_collection.gooses["Крикун"].honk_volume == 10

    def test_goose_registry_invalid_type(self):
        """Тестирует ошибку при регистрации гуся с неверным типом."""
        casino = Casino()
        with pytest.raises(TypeError):
            casino.goose_registry("InvalidGoose", "Неверныйгусь", 100)

    def test_calculate_k_range(self):
        """Тестирует, что коэффициент находится в допустимом диапазоне."""
        casino = Casino(seed=42)
        
        for _ in range(100):
            k = casino.calculate_k()
            assert 0.7 <= k <= 10

    def test_lay_out_for_chips(self):
        """Тестирует конвертацию значения в фишки."""
        casino = Casino()
        
        chips = casino.lay_out_for_chips(100)
        total_value = sum(chip.value for chip in chips)
        assert total_value == 100
        
        chips = casino.lay_out_for_chips(500)
        total_value = sum(chip.value for chip in chips)
        assert total_value == 500

    def test_summary_players_balance(self):
        """Тестирует подсчёт общего баланса игроков."""
        casino = Casino()
        
        casino.player_registry("Игрок1", 1000)
        casino.player_registry("Игрок2", 2000)
        
        expected_balance = 1000 + 2000
        assert casino.summary_players_balance == expected_balance


class TestCasinoIntegration:
    """Интеграционные тесты для всей системы казино."""

    def test_full_game_setup(self):
        """Тестирует полную настройку игры."""
        casino = Casino(seed=42)
        
        casino.player_registry("Алиса", 1500)
        casino.player_registry("Боб", 2000)
        
        casino.goose_registry("Goose", "Мирный", 500)
        casino.goose_registry("WarGoose", "Агрессивный", 800)
        casino.goose_registry("HonkGoose", "Шумный", 600)
        
        assert len(casino.player_collection) == 2
        assert len(casino.goose_collection) == 3
        assert casino.summary_players_balance == 3500
        
        assert isinstance(casino.goose_collection.gooses["Мирный"], Goose)
        assert isinstance(casino.goose_collection.gooses["Агрессивный"], WarGoose)
        assert isinstance(casino.goose_collection.gooses["Шумный"], HonkGoose)

    def test_player_bet_and_balance_change(self):
        """Тестирует ставки игроков и изменение баланса."""
        casino = Casino(seed=42)
        casino.player_registry("Игрок", 1000)
        
        player = casino.player_collection["Игрок"]
        initial_chip_count = len(player.chips_col)
        initial_balance = player.balance
        
        if initial_balance > 0:
            bet = player.make_bet()
            assert bet > 0
            assert player.balance == initial_balance - bet
            assert len(player.chips_col) == initial_chip_count - 1