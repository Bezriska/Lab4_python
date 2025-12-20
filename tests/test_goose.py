
import pytest

from src.classes.GooseClasess import Goose, WarGoose, HonkGoose, GooseFlock


class TestGoose:
    """Тесты для базового класса Goose."""

    def test_goose_creation(self):
        """Тестирует создание базового гуся."""
        goose = Goose("Серый", 100)
        assert goose.name == "Серый"
        assert goose.balance == 100

    def test_goose_creation_default_balance(self):
        """Тестирует создание гуся с балансом по умолчанию."""
        goose = Goose("Белый")
        assert goose.name == "Белый"
        assert goose.balance == 0

    def test_goose_repr(self):
        """Тестирует строковое представление гуся."""
        goose = Goose("Серый", 100)
        expected = "Goose(name = 'Серый', balance = 100)"
        assert repr(goose) == expected

    def test_goose_addition_same_type(self):
        """Тестирует объединение двух обычных гусей."""
        goose1 = Goose("Серый", 100)
        goose2 = Goose("Белый", 200)
        
        initial_ids_count = len(Goose.lst_id)
        
        flock = goose1 + goose2
        assert isinstance(flock, GooseFlock)
        assert flock.balance == 300
        assert flock.type == "Goose"
        assert len(Goose.lst_id) == initial_ids_count - 1


class TestWarGoose:
    """Тесты для класса WarGoose."""

    def test_war_goose_creation(self):
        """Тестирует создание боевого гуся."""
        goose = WarGoose("Боец", 150)
        assert goose.name == "Боец"
        assert goose.balance == 150
        assert goose.damage == 10

    def test_war_goose_repr(self):
        """Тестирует строковое представление боевого гуся."""
        goose = WarGoose("Боец", 150)
        expected = "WarGoose(name = 'Боец', balance = 150)"
        assert repr(goose) == expected

    def test_war_goose_addition_same_type(self):
        """Тестирует объединение двух боевых гусей."""
        goose1 = WarGoose("Боец1", 100)
        goose2 = WarGoose("Боец2", 200)
        
        initial_ids_count = len(Goose.lst_id)
        
        flock = goose1 + goose2
        assert isinstance(flock, GooseFlock)
        assert flock.balance == 300
        assert flock.damage == 20
        assert flock.type == "WarGoose"
        assert len(Goose.lst_id) == initial_ids_count - 1

    def test_war_goose_addition_different_type(self):
        """Тестирует ошибку при попытке объединить боевого гуся с другим типом."""
        war_goose = WarGoose("Боец", 100)
        regular_goose = Goose("Обычный", 100)
        
        with pytest.raises(TypeError):
            war_goose + regular_goose


class TestHonkGoose:
    """Тесты для класса HonkGoose."""

    def test_honk_goose_creation(self):
        """Тестирует создание кричащего гуся."""
        goose = HonkGoose("Крикун", 120)
        assert goose.name == "Крикун"
        assert goose.balance == 120
        assert goose.honk_volume == 10

    def test_honk_goose_repr(self):
        """Тестирует строковое представление кричащего гуся."""
        goose = HonkGoose("Крикун", 120)
        expected = "HonkGoose(name = 'Крикун', balance = 120)"
        assert repr(goose) == expected

    def test_honk_goose_addition_same_type(self):
        """Тестирует объединение двух кричащих гусей."""
        goose1 = HonkGoose("Крикун1", 100)
        goose2 = HonkGoose("Крикун2", 200)
        
        initial_ids_count = len(Goose.lst_id)
        
        flock = goose1 + goose2
        assert isinstance(flock, GooseFlock)
        assert flock.balance == 300
        assert flock.honk_volume == 20
        assert flock.type == "HonkGoose"
        assert len(Goose.lst_id) == initial_ids_count - 1


class TestGooseFlock:
    """Тесты для класса GooseFlock."""

    def test_goose_flock_creation(self):
        """Тестирует создание стаи гусей."""
        flock = GooseFlock("Стая1", 500, "Goose")
        assert flock.name == "Стая1"
        assert flock.balance == 500
        assert flock.type == "Goose"
        assert flock.damage == 0
        assert flock.honk_volume == 0

    def test_war_goose_flock_creation(self):
        """Тестирует создание стаи боевых гусей."""
        flock = GooseFlock("БоеваяСтая", 600, "WarGoose", damage=25)
        assert flock.name == "БоеваяСтая"
        assert flock.balance == 600
        assert flock.type == "WarGoose"
        assert flock.damage == 25

    def test_honk_goose_flock_creation(self):
        """Тестирует создание стаи кричащих гусей."""
        flock = GooseFlock("КричащаяСтая", 400, "HonkGoose", honk_volume=30)
        assert flock.name == "КричащаяСтая"
        assert flock.balance == 400
        assert flock.type == "HonkGoose"
        assert flock.honk_volume == 30

    def test_flock_repr_regular(self):
        """Тестирует строковое представление обычной стаи."""
        flock = GooseFlock("Стая1", 500, "Goose")
        expected = "GooseFlock(name = 'Стая1', balance = 500, type = 'Goose')"
        assert repr(flock) == expected

    def test_flock_repr_war(self):
        """Тестирует строковое представление боевой стаи."""
        flock = GooseFlock("БоеваяСтая", 600, "WarGoose", damage=25)
        expected = "WarGooseFlock(name = 'БоеваяСтая', balance = 600, type = 'WarGoose', damage = 25)"
        assert repr(flock) == expected

    def test_flock_repr_honk(self):
        """Тестирует строковое представление кричащей стаи."""
        flock = GooseFlock("КричащаяСтая", 400, "HonkGoose", honk_volume=30)
        expected = "HonkGooseFlock(name = 'КричащаяСтая', balance = 400, type = 'HonkGoose', honk volume = 30)"
        assert repr(flock) == expected

    def test_flock_add_goose(self):
        """Тестирует добавление гуся в стаю."""
        flock = GooseFlock("Стая1", 500, "Goose")
        new_goose = Goose("Новый", 100)
        
        updated_flock = flock + new_goose
        assert updated_flock.balance == 600
        assert updated_flock is flock