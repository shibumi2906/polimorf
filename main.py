class Animal:             # создаём базовый класс
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):   #
        pass

    def eat(self):                #
        print(f"{self.name} ест.")

class Bird(Animal):
    def make_sound(self):               # птички говорят чирик
        print(f"{self.name} чирик.")

class Mammal(Animal):                  # млекопитающие говорят рррр
    def make_sound(self):
        print(f"{self.name} рррр.")

class Reptile(Animal):             #рептилии говорят шшшшш
    def make_sound(self):
        print(f"{self.name} шшшшш.")

def animal_sound(animals):       # цикл фор заставляет всех говорить своё
    for animal in animals:
        animal.make_sound()


class Zoo:         #создаём класс зоо
    def __init__(self):       # создаём список животных и список сорудников
        self.animals = []
        self.staff = []

    def add_animal(self, animal):       # функция добавления животного
        self.animals.append(animal)
        print(f"{animal.name} успешно добавлено zoo.")

    def add_staff(self, staff_member):  # функция добавления сотрудника
        self.staff.append(staff_member)
        print(f"{staff_member.name} успешно добавлен zoo.")

class ZooKeeper:                   # класс зооработников
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}.")

class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}.")

# Создаем объекты животных
bird = Bird("Tweety", 1)
dog = Mammal("Rex", 5)
snake = Reptile("Sly", 2)

# Демонстрация полиморфизма
animals = [bird, dog, snake]
animal_sound(animals)

# Создаем зоопарк
zoo = Zoo()

# Добавляем животных и сотрудников в зоопарк
zoo.add_animal(bird)
zoo.add_animal(dog)
zoo_keeper = ZooKeeper("John")
veterinarian = Veterinarian("Dr. Smith")
zoo.add_staff(zoo_keeper)
zoo.add_staff(veterinarian)

# Сотрудники выполняют свои действия
zoo_keeper.feed_animal(snake)
veterinarian.heal_animal(bird)





