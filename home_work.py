# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты
# (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
#
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`,
# которые наследуют от класса `Animal`. Добавьте специфические атрибуты и переопределите методы, если требуется
# (например, различный звук для `make_sound()`).
#
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
#
# 4. Используйте композицию для создания класса `Zoo`,
# который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.
#
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`,
# которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()`
# для `Veterinarian`).

# Базовый класс Animal


import pickle  # модуль для работы с загрузкой/выгрузкой кода в файл


class Animal(): # базовый класс
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self): # звук животного заглушен, так как будет переопределен в подклассах
        pass

    def eat(self):
        print(f"{self.name} ест")

    def walk(self): # стиль ходьбы заглушен, так как будет переопределен в подклассах
        pass

class Bird(Animal):  # Подкласс Bird, наследующий от Animal
    def __init__(self, name, age, size):
        super().__init__(name, age)
        self.size = size

    def make_sound(self):
        print(f"{self.name} чирикает")
    def walk(self):
        print(f"{self.name} летает")

class Mammal(Animal): # Подкласс Mammal, наследующий от Animal
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} рычит")

    def walk(self):
        print(f"{self.name} бегает")

class Cat(Mammal): # подкласс Cat наследующий от Mammal для переопределения звука кошки.
    def __init__(self, name, age,fur_color):
        super().__init__(name,age,fur_color)
    def make_sound(self):
        print(f"{self.name} мяукает")



class Reptile(Animal):  # Подкласс Reptile, наследующий от Animal
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        print(f"{self.name} шипит")
    def walk(self):
        print(f"{self.name} ползает")


def animal_sound(animals): # Функция для демонстрации полиморфизма
    for animal in animals:
        animal.eat()
        animal.make_sound()
        animal.walk()

# Класс для сотрудников зоопарка
class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}")

class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}")


class Zoo:  # Класс Zoo, использующий композицию
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff_member):
        self.staff.append(staff_member)

    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)
        print("Zoo state saved to file.")

    @staticmethod
    def load_from_file(filename):
        try:
            with open(filename, 'rb') as file:
                zoo = pickle.load(file)
            print("Zoo state loaded from file.")
            return zoo
        except FileNotFoundError:
            print("File not found. Returning an empty zoo.")
            return Zoo()


if __name__ == "__main__":
    # Загружаем состояние зоопарка из файла
   zoo = Zoo.load_from_file('zoo_state.pkl')
   if not zoo.animals and not zoo.staff:

    # Создаем животных

    sparrow = Bird("Вася", 2, "Маленький")
    tiger = Mammal("Гриша", 5, "Желтый")
    snake = Reptile("Гена", 3, "Гладкий")
    cat = Cat("Мурка",5, "Коричневый")

    # Создаем сотрудников
    zookeeper = ZooKeeper("Иван")
    vet = Veterinarian("Юлия")

    # Создаем зоопарк и добавляем животных и сотрудников
    zoo = Zoo()
    zoo.add_animal(sparrow)
    zoo.add_animal(tiger)
    zoo.add_animal(snake)
    zoo.add_animal(cat)
    zoo.add_staff(zookeeper)
    zoo.add_staff(vet)

    # Демонстрируем полиморфизм
    animal_sound(zoo.animals)

    # Используем методы сотрудников
    zookeeper.feed_animal(tiger)
    vet.heal_animal(snake)

    # Сохраняем состояние зоопарка в файл
    # zoo.save_to_file('zoo_state.pkl')






