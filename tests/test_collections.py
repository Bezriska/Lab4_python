
import pytest


from src.collections.CasinoBalanceCollection import CasinoBalance
from src.collections.GooseCollection import GooseCollection
from src.classes.PlayerClass import Player
from src.classes.GooseClasess import Goose, WarGoose, HonkGoose


class TestCasinoBalance:
    """Тесты для коллекции игроков CasinoBalance."""

    def test_empty_collection(self):
        """Тестирует создание пустой коллекции."""
        collection = CasinoBalance()
        assert len(collection) == 0
        assert collection.summary_balance == 0
        assert len(collection.players) == 0

    def test_add_player(self):
        """Тестирует добавление игрока."""
        collection = CasinoBalance()
        player = Player("Тест")
        collection.add_player(player)
        
        assert len(collection) == 1
        assert "Тест" in collection.players
        assert collection["Тест"] == player

    def test_remove_player(self):
        """Тестирует удаление игрока."""
        collection = CasinoBalance()
        player = Player("Тест")
        collection.add_player(player)
        
        assert len(collection) == 1
        collection.rm_player("Тест")
        assert len(collection) == 0

    def test_remove_nonexistent_player(self):
        """Тестирует ошибку при удалении несуществующего игрока."""
        collection = CasinoBalance()
        with pytest.raises(KeyError):
            collection.rm_player("НесуществующийИгрок")

    def test_get_nonexistent_player(self):
        """Тестирует ошибку при получении несуществующего игрока."""
        collection = CasinoBalance()
        with pytest.raises(KeyError):
            player = collection["Несуществующийигрок"]

    def test_summary_balance(self):
        """Тестирует подсчёт общего баланса."""
        collection = CasinoBalance()
        player1 = Player("Игрок1")
        player2 = Player("Игрок2")
        
        from src.classes.ChipClass import Chip
        player1.chips_col.add_chip(Chip(100))
        player2.chips_col.add_chip(Chip(200))
        
        collection.add_player(player1)
        collection.add_player(player2)
        
        assert collection.summary_balance == 300

    def test_iteration(self):
        """Тестирует итерацию по коллекции."""
        collection = CasinoBalance()
        players = [Player("Игрок1"), Player("Игрок2")]
        
        for player in players:
            collection.add_player(player)
        
        player_names = list(collection)
        assert len(player_names) == 2
        assert "Игрок1" in player_names
        assert "Игрок2" in player_names


class TestGooseCollection:
    """Тесты для коллекции гусей GooseCollection."""

    def test_empty_collection(self):
        """Тестирует создание пустой коллекции гусей."""
        collection = GooseCollection()
        assert len(collection) == 0
        assert len(collection.gooses) == 0
        assert len(collection.flockes) == 0
        assert collection.summary_goose_balance == 0

    def test_add_goose(self):
        """Тестирует добавление гуся."""
        collection = GooseCollection()
        goose = Goose("Тестовый", 100)
        collection.add_goose(goose)
        
        assert len(collection) == 1
        assert "Тестовый" in collection.gooses
        assert collection["Тестовый"] == goose

    def test_add_war_goose(self):
        """Тестирует добавление боевого гуся."""
        collection = GooseCollection()
        war_goose = WarGoose("Боец", 200)
        collection.add_goose(war_goose)
        
        assert len(collection) == 1
        assert "Боец" in collection.gooses
        assert isinstance(collection.gooses["Боец"], WarGoose)
        assert collection.gooses["Боец"].damage == 10

    def test_add_honk_goose(self):
        """Тестирует добавление кричащего гуся."""
        collection = GooseCollection()
        honk_goose = HonkGoose("Крикун", 150)
        collection.add_goose(honk_goose)
        
        assert len(collection) == 1
        assert "Крикун" in collection.gooses
        assert isinstance(collection.gooses["Крикун"], HonkGoose)
        assert collection.gooses["Крикун"].honk_volume == 10

    def test_summary_balance_only_gooses(self):
        """Тестирует подсчёт баланса только с гусями."""
        collection = GooseCollection()
        collection.add_goose(Goose("Гусь1", 100))
        collection.add_goose(Goose("Гусь2", 200))
        
        assert collection.summary_goose_balance == 300

    def test_remove_goose(self):
        """Тестирует удаление гуся."""
        collection = GooseCollection()
        goose = Goose("Тест", 100)
        collection.add_goose(goose)
        
        assert len(collection) == 1
        collection.rm_goose("Тест")
        assert len(collection) == 0

    def test_get_nonexistent_goose(self):
        """Тестирует ошибку при получении несуществующего гуся."""
        collection = GooseCollection()
        with pytest.raises(KeyError):
            goose = collection["НесуществующийГусь"]

    def test_multiple_goose_types(self):
        """Тестирует работу с разными типами гусей."""
        collection = GooseCollection()
        
        regular_goose = Goose("Обычный", 100)
        war_goose = WarGoose("Боевой", 200)
        honk_goose = HonkGoose("Кричащий", 150)
        
        collection.add_goose(regular_goose)
        collection.add_goose(war_goose)
        collection.add_goose(honk_goose)
        
        assert len(collection) == 3
        assert collection.summary_goose_balance == 450
        
        assert isinstance(collection["Обычный"], Goose)
        assert isinstance(collection["Боевой"], WarGoose)
        assert isinstance(collection["Кричащий"], HonkGoose)

    def test_make_flock_insufficient_gooses(self):
        """Тестирует ошибку при создании стаи из менее чем 2 гусей."""
        collection = GooseCollection()
        goose = Goose("Одинокий", 100)
        collection.add_goose(goose)
        
        with pytest.raises(ValueError):
            collection.make_flock(["Одинокий"])

    def test_make_flock_two_gooses(self):
        """Тестирует создание стаи из двух гусей."""
        collection = GooseCollection()
        
        goose1 = Goose("Гусь1", 100)
        goose2 = Goose("Гусь2", 200)
        collection.add_goose(goose1)
        collection.add_goose(goose2)
        
        flock = collection.make_flock(["Гусь1", "Гусь2"])
        
        assert isinstance(flock, type(goose1 + goose2))
        assert flock.balance == 300
        
        assert len(collection.gooses) == 0
        assert len(collection.flockes) == 1

    def test_make_flock_multiple_gooses(self):
        """Тестирует создание стаи из нескольких гусей."""
        collection = GooseCollection()
        
        for i in range(1, 4):
            goose = Goose(f"Гусь{i}", 100 * i)
            collection.add_goose(goose)
        
        flock = collection.make_flock(["Гусь1", "Гусь2", "Гусь3"])
        
        assert flock.balance == 600
        assert len(collection.gooses) == 0
        assert len(collection.flockes) == 1

    def test_set_goose_balance(self):
        """Тестирует изменение баланса гуся."""
        collection = GooseCollection()
        goose = Goose("Тест", 100)
        collection.add_goose(goose)
        
        collection["Тест"] = 500
        assert collection.gooses["Тест"].balance == 500

    def test_summary_balance_with_flock(self):
        """Тестирует подсчёт баланса с учётом стай."""
        collection = GooseCollection()
        
        single_goose = Goose("Одиночка", 100)
        collection.add_goose(single_goose)
        
        goose1 = Goose("Гусь1", 200)
        goose2 = Goose("Гусь2", 300)
        collection.add_goose(goose1)
        collection.add_goose(goose2)
        flock = collection.make_flock(["Гусь1", "Гусь2"])
        
        assert collection.summary_goose_balance == 600