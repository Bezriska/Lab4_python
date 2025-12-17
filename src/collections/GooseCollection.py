from src.logger import logger
from src.classes.GooseClasess import Goose, WarGoose, HonkGoose


class GooseCollection:
    """Коллекция для управления гусями и их стаями.
    
    Attributes:
        gooses: Словарь отдельных гусей
        flockes: Словарь стай гусей
    """

    def __init__(self) -> None:
        """Инициализирует пустую коллекцию гусей."""

        self.gooses = {}
        self.flockes = {}

    @property
    def summary_goose_balance(self):
        """Вычисляет суммарный баланс всех гусей и стай.
        
        Returns:
            float: Общий баланс гусей и стай
        """
        goose_balance = sum(goose.balance for goose in self.gooses.values())
        flock_balance = sum(flock.balance for flock in self.flockes.values())
        return goose_balance + flock_balance

    def __iter__(self):
        """Возвращает итератор по именам гусей.
        
        Returns:
            iterator: Итератор по ключам словаря гусей
        """
        return iter(self.gooses)

    def __len__(self) -> int:
        """Возвращает количество гусей в коллекции.
        
        Returns:
            int: Количество гусей (без учета стай)
        """
        return len(self.gooses)

    def __getitem__(self, name):
        """Получает гуся по имени.
        
        Args:
            name: Имя гуся
            
        Returns:
            Goose: Объект гуся
            
        Raises:
            KeyError: Если гусь с таким именем не найден
        """
        if name in self.gooses:
            return self.gooses[name]
        else:
            logger.error(f"Goose with name {name} does not found")
            raise KeyError(f"Goose with name {name} does not found")

    def __setitem__(self, name, balance):
        """Устанавливает новый баланс гусю.
        
        Args:
            name: Имя гуся
            balance: Новый баланс
        """
        bal = self.gooses[name].balance
        self.gooses[name].balance = balance
        logger.info(
            f"{name}'s balance has been changed from {bal} to {balance}")

    def add_goose(self, goose: Goose | WarGoose | HonkGoose):
        """Добавляет гуся в коллекцию.
        
        Args:
            goose: Объект гуся для добавления
        """
        self.gooses[goose.name] = goose

    def rm_goose(self, name):
        """Удаляет гуся из коллекции.
        
        Args:
            name: Имя гуся для удаления
            
        Raises:
            KeyError: Если гусь с таким именем не найден
        """
        if name in self.gooses:
            del self.gooses[name]
        else:
            logger.error("Incorrect name")
            raise KeyError("Incorrect name")

    def make_flock(self, gooses_names: list[str]):
        """Создает стаю из нескольких гусей одного типа.
        
        Args:
            gooses_names: Список имен гусей для объединения в стаю
            
        Returns:
            GooseFlock: Созданная стая гусей
            
        Raises:
            ValueError: Если передано меньше 2 гусей
            TypeError: Если гуси разных типов
        """
        if len(gooses_names) < 2:
            raise ValueError("Flock include min 2 gooses")

        flock = self.gooses[gooses_names[0]] + self.gooses[gooses_names[1]]

        self.rm_goose(gooses_names[0])
        self.rm_goose(gooses_names[1])

        for name in gooses_names[2:]:
            flock += self.gooses[name]
            self.rm_goose(name)

        self.flockes[flock.name] = flock

        return flock

