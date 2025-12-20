import pytest

from src.classes.ChipClass import Chip
from src.collections.ChipCollection import ChipCollection


class TestChip:
    """Тесты для класса Chip."""

    def test_chip_creation(self):
        """Тестирует создание фишки."""
        chip = Chip(100)
        assert chip.value == 100

    def test_chip_addition(self):
        """Тестирует сложение фишек."""
        chip1 = Chip(100)
        chip2 = Chip(200)
        result = chip1 + chip2
        assert result.value == 300
        assert isinstance(result, Chip)

    def test_chip_addition_with_wrong_type(self):
        """Тестирует ошибку при сложении фишки с другим типом."""
        chip = Chip(100)
        with pytest.raises(TypeError):
            chip + 50

    def test_chip_repr(self):
        """Тестирует строковое представление фишки."""
        chip = Chip(100)
        assert repr(chip) == "Chip(100)"


class TestChipCollection:
    """Тесты для класса ChipCollection."""

    def test_empty_collection(self):
        """Тестирует создание пустой коллекции."""
        collection = ChipCollection()
        assert len(collection) == 0
        assert collection.summary_value == 0

    def test_add_chip(self):
        """Тестирует добавление фишки в коллекцию."""
        collection = ChipCollection()
        chip = Chip(100)
        collection.add_chip(chip)
        assert len(collection) == 1
        assert collection.summary_value == 100

    def test_summary_value(self):
        """Тестирует подсчёт общей стоимости фишек."""
        collection = ChipCollection()
        collection.add_chip(Chip(100))
        collection.add_chip(Chip(200))
        collection.add_chip(Chip(50))
        assert collection.summary_value == 350

    def test_iteration(self):
        """Тестирует итерацию по коллекции."""
        collection = ChipCollection()
        chips = [Chip(100), Chip(200)]
        for chip in chips:
            collection.add_chip(chip)
        
        collected_chips = list(collection)
        assert len(collected_chips) == 2
        assert all(isinstance(chip, Chip) for chip in collected_chips)

    def test_getitem(self):
        """Тестирует получение элементов по индексу."""
        collection = ChipCollection()
        collection.add_chip(Chip(100))
        collection.add_chip(Chip(200))
        
        first_chips = collection.chips[0:1]
        assert len(first_chips) == 1
        assert first_chips[0].value == 100

    def test_add_many_chips(self):
        """Тестирует добавление нескольких фишек сразу."""
        collection = ChipCollection()
        chips = [Chip(100), Chip(200), Chip(50)]
        collection.add_many_chips(chips)
        
        assert len(collection) == 3
        assert collection.summary_value == 350

    def test_remove_chip(self):
        """Тестирует удаление фишки по номиналу."""
        collection = ChipCollection()
        collection.add_chip(Chip(100))
        collection.add_chip(Chip(200))
        collection.add_chip(Chip(100))
        
        assert len(collection) == 3
        collection.remove_chip(100)
        assert len(collection) == 2
        assert collection.summary_value == 300

    def test_remove_nonexistent_chip(self):
        """Тестирует ошибку при удалении несуществующей фишки."""
        collection = ChipCollection()
        collection.add_chip(Chip(100))
        
        with pytest.raises(ValueError):
            collection.remove_chip(500)

    def test_repr(self):
        """Тестирует строковое представление коллекции."""
        collection = ChipCollection()
        collection.add_chip(Chip(100))
        collection.add_chip(Chip(200))
        
        expected = f"ChipCollection(chips={collection.chips}, total=300)"
        assert repr(collection) == expected