import random


class Goose:
    """Базовый класс для гуся.
    
    Attributes:
        lst_id: Список доступных ID для стай гусей
        name: Имя гуся
        balance: Баланс гуся
    """

    lst_id = random.sample(range(0, 50), 10)

    def __init__(self, name, balance: int = 0) -> None:
        """Инициализирует гуся с именем и балансом.
        
        Args:
            name: Имя гуся
            balance: Начальный баланс гуся (по умолчанию 0)
        """

        self.name: str | None = name
        self.balance = balance

    def __repr__(self):
        """Возвращает строковое представление гуся.
        
        Returns:
            str: Строка с типом, именем и балансом гуся
        """
        return f"{type(self).__name__}(name = '{self.name}', balance = {self.balance})"

    def __add__(self, other):
        """Объединяет двух гусей одного типа в стаю.
        
        Args:
            other: Другой гусь для объединения
            
        Returns:
            GooseFlock: Новая стая гусей
            
        Raises:
            TypeError: Если гуси разных типов
        """
        if type(self).__name__ == "Goose" and type(other).__name__ == type(self).__name__:
            flock_id = random.choice(Goose.lst_id)
            Goose.lst_id.remove(flock_id)
        else:
            raise TypeError("You can concatenate only identical gooses type")

        return GooseFlock(f"Flock{flock_id}", (self.balance + other.balance), type(self).__name__)


class WarGoose(Goose):
    """Боевой гусь, который может атаковать игроков.
    
    Attributes:
        damage: Урон, наносимый гусем при атаке
    """

    def __init__(self, name, balance: int = 0) -> None:
        """Инициализирует боевого гуся.
        
        Args:
            name: Имя гуся
            balance: Начальный баланс гуся (по умолчанию 0)
        """
        super().__init__(name, balance)
        self.damage = 10

    def __add__(self, other):
        if type(self).__name__ == "WarGoose" and type(other).__name__ == type(self).__name__:
            flock_id = random.choice(Goose.lst_id)
            Goose.lst_id.remove(flock_id)
        else:
            raise TypeError("You can concatenate only identical gooses type")

        return GooseFlock(f"Flock{flock_id}", (self.balance + other.balance), type(self).__name__, self.damage + other.damage)


class HonkGoose(Goose):
    """Кричащий гусь, который повышает уровень паники игроков.
    
    Attributes:
        honk_volume: Громкость крика, увеличивающая панику
    """

    def __init__(self, name, balance: int = 0) -> None:
        """Инициализирует кричащего гуся.
        
        Args:
            name: Имя гуся
            balance: Начальный баланс гуся (по умолчанию 0)
        """
        super().__init__(name, balance)
        self.honk_volume = 10

    def __add__(self, other):
        if type(self).__name__ == "HonkGoose" and type(other).__name__ == type(self).__name__:
            flock_id = random.choice(Goose.lst_id)
            Goose.lst_id.remove(flock_id)
        else:
            raise TypeError("You can concatenate only identical gooses type")

        return GooseFlock(f"Flock{flock_id}", (self.balance + other.balance), type(self).__name__, honk_volume=self.honk_volume + other.honk_volume)


class GooseFlock:
    """Стая гусей одного типа.
    
    Attributes:
        flock: Словарь с информацией о стае
        balance: Общий баланс стаи
        name: Название стаи
        type: Тип гусей в стае
        damage: Урон стаи (для боевых гусей)
        honk_volume: Громкость крика стаи (для кричащих гусей)
    """

    def __init__(self, name, balance, goose_type, damage=0, honk_volume=0) -> None:
        """Инициализирует стаю гусей.
        
        Args:
            name: Название стаи
            balance: Начальный баланс стаи
            goose_type: Тип гусей в стае
            damage: Урон стаи (по умолчанию 0)
            honk_volume: Громкость крика стаи (по умолчанию 0)
        """

        self.flock = {}
        self.balance = balance
        self.name = name
        self.flock[name] = self.balance
        self.type = goose_type
        self.damage = damage
        self.honk_volume = honk_volume

    def __repr__(self) -> str:
        """Возвращает строковое представление стаи гусей.
        
        Returns:
            str: Строка с информацией о стае в зависимости от типа
        """
        if self.type == "Goose":
            return f"GooseFlock(name = '{self.name}', balance = {self.balance}, type = '{self.type}')"
        elif self.type == "WarGoose":
            return f"WarGooseFlock(name = '{self.name}', balance = {self.balance}, type = '{self.type}', damage = {self.damage})"
        else:
            return f"HonkGooseFlock(name = '{self.name}', balance = {self.balance}, type = '{self.type}', honk volume = {self.honk_volume})"

    def __add__(self: "GooseFlock", other: WarGoose | HonkGoose | Goose):
        """Добавляет гуся в существующую стаю.
        
        Args:
            other: Гусь для добавления в стаю
            
        Returns:
            GooseFlock: Обновленная стая
        """
        self.balance += other.balance
        self.flock[self.name] = self.balance
        return self
