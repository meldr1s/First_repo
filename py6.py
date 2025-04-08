# class User:
#     name = 'Anonymous'
#     age = 15

# user1 = User()
# print(user1.name)
# print(user1.age)

# user2 = User()
# user2.name = "John"
# user2.age = 90

# print(user2.name)
# print(user2.age)

# class Person:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age

#     def say_name(self) -> None:
#         print(f'Hi! I am {self.name} and I am {self.age} years old.')

#     def set_age(self, age: int) -> None:
#         self.age = age

# bob = Person('Boris', 34)

# bob.say_name()
# bob.set_age(25)
# bob.say_name()

# class Person:
#     count = 0

#     def __init__(self, name: str):
#         self.name = name
#         Person.count += 1

#     def how_many_persons(self):
#         print(f"Кількість людей зараз {Person.count}")

# first = Person('Boris')
# first.how_many_persons()
# second = Person('Alex')
# first.how_many_persons()

# class Pokemon:
#     def __init__(self, name, type, health):
#         self.name = name
#         self.type = type
#         self.health = health

#     def attack(self, other_pokemon):
#         print(f"{self.name} attacks {other_pokemon.name}!")

#     def dodge(self):
#         print(f"{self.name} dodged the attack!")

#     def evolve(self, new_form):
#         print(f"{self.name} is evolving into {new_form}!")
#         self.name = new_form

# # Створення об'єкта Pikachu
# pikachu = Pokemon("Pikachu", "Electric", 100)

# # Використання методів
# pikachu.attack(Pokemon("Charmander", "Fire", 100))
# pikachu.dodge()
# pikachu.evolve("Raichu")

# def __init__(self, name, type, health):
#         self.name = name  # Ініціалізація атрибута імені
#         self.type = type  # Ініціалізація атрибута типу
#         self.health = health  # Ініціалізація атрибута здоров'я

# class Person:
#     def __init__(self, name: str, age: int, is_active: bool):
#         self.name = name
#         self.age = age
#         self._is_active = is_active

#     def greeting(self):
#         return f"Hi {self.name}"

# p = Person("Boris", 34, True)
# print(p.name, p.age, p._is_active)
# print(p.greeting())

# class Person:
#     def __init__(self, name: str, age: int, is_active: bool):
#         self.name = name
#         self.age = age
#         self._is_active = is_active

#     def greeting(self):
#         return f"Hi {self.name}"
    
#     def is_active(self):
#         return self._is_active

#     def set_active(self, active: bool):
#         self._is_active = active

# p = Person("Boris", 34, True)
# print(p.name, p.age, p.is_active())
# print(p.greeting())

# class Person:
#     def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
#         self.name = name
#         self.age = age
#         self._is_active = is_active
#         self.__is_admin = is_admin

#     def greeting(self):
#         return f"Hi {self.name}"

#     def is_active(self):
#         return self._is_active

#     def set_active(self, active: bool):
#         self._is_active = active

# p = Person("Boris", 34, True, False)
# print(p.__is_admin)

# class Person:
#     def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
#         self.name = name
#         self.age = age
#         self._is_active = is_active
#         self.__is_admin = is_admin

#     def greeting(self):
#         return f"Hi {self.name}"

#     def is_active(self):
#         return self._is_active

#     def set_active(self, active: bool):
#         self._is_active = active

# p = Person("Boris", 34, True, False)
# print(p._Person__is_admin)

# class Person:
#     def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
#         self.name = name
#         self.age = age
#         self._is_active = is_active
#         self.__is_admin = is_admin

#     def greeting(self):
#         return f"Hi {self.name}"

#     def is_active(self):
#         return self._is_active

#     def set_active(self, active: bool):
#         self._is_active = active

#     def get_is_admin(self):
#         return self.__is_admin

#     def set_is_admin(self, is_admin: bool):
#         # Тут можна додати будь-яку логіку перевірки або обробки
#         self.__is_admin = is_admin

        
# p = Person("Boris", 34, True, False)
# print(p.get_is_admin())
# p.set_is_admin(True)
# print(p.get_is_admin())

# class Animal:
#     def __init__(self, nickname: str, age: int):
#         self.nickname = nickname
#         self.age = age

#     def make_sound(self):
#         pass

# class Cat(Animal):
#     def make_sound(self) -> str:
#         return "Meow"

# class Dog(Animal):
#     def make_sound(self) -> str:
#         return "Woof"

# class Cow(Animal):  
#     def make_sound(self):
#         return "Moo"

# my_cat = Cat("Simon", 4)
# my_dog = Dog("Rex", 5)
# my_cow = Cow("Bessie", 3)

# print(my_cat.make_sound())  # Виведе "Meow"
# print(my_dog.make_sound())  # Виведе "Woof"
# print(my_cow.make_sound())  # Виведе "Moo"

# class Animal:
#     def __init__(self, nickname: str, age: int):
#         self.nickname = nickname
#         self.age = age

#     def make_sound(self):
#         pass

# class Cat(Animal):
#     def make_sound(self) -> str:
#         return "Meow"

# class Dog(Animal):

#     def __init__(self, nickname: str, age: int, breed: str):
#         super().__init__(nickname, age)  # Викликаємо конструктор базового класу
#         self.breed = breed  # Додаємо нову властивість

#     def make_sound(self) -> str:
#         return "Woof"

#     def chase_tail(self) -> str:
#         return f"{self.nickname} is chasing its tail!"

# class Cow(Animal):
#     def make_sound(self):
#         return "Moo"

# my_cat = Cat("Simon", 4)
# my_cow = Cow("Bessie", 3)

# print(my_cat.make_sound())  # Виведе "Meow"
# print(my_cow.make_sound())  # Виведе "Moo"

# my_dog = Dog("Rex", 5, "Golden Retriever")
# print(my_dog.make_sound())  # Виведе "Woof"
# print(my_dog.chase_tail())  # Виведе "Rex is chasing its tail!"

# class Animal:
#     def __init__(self, nickname: str, age: int):
#         self.nickname = nickname
#         self.age = age

#     def make_sound(self):
#         pass

# class Bird(Animal):
#     def make_sound(self):
#         return "Chirp"

# class Parrot(Bird):
#     def can_fly(self):
#         return True

# class TalkingParrot(Parrot):
#     def say_phrase(self, phrase):
#         return f"The parrot says: '{phrase}'"

# my_parrot = TalkingParrot("Alice", 2)
# print(my_parrot.make_sound())
# print(my_parrot.can_fly())
# print(my_parrot.say_phrase("Hello, World!"))

# class A:
#     pass

# class B(A):
#     pass

# class C(A):
#     pass

# class D(B, C):
#     pass

# print(D.mro())  # Виведе порядок розв'язання методів для класу D

# class A:
#     name = "Я клас A"

# class B:
#     name = "Я клас B"
#     property = "Я знаходжусь в класі B"

# class C(A, B):
#     property = "Я знаходжусь в класі C"

# c = C()
# print(c.name)
# print(c.property)

# class A:
#     name = "Я клас A"

# class B:
#     name = "Я клас B"
#     property = "Я знаходжусь в класі B"

# class C(B, A):
#     property = "Я знаходжусь в класі C"

# c = C()
# print(c.name)
# print(c.property)

# class Animal:
#     def __init__(self, nickname: str, age: int):
#         self.nickname = nickname
#         self.age = age

#     def make_sound(self):
#         pass

# class Cat(Animal):
#     def make_sound(self):
#         return "Meow"

# class Dog(Animal):
#     def make_sound(self):
#         return "Woof"

# def animal_sounds(animals):
#     for animal in animals:
#         print(animal.make_sound())

# animals = [Cat("Simon", 4), Dog("Rex", 5)]
# animal_sounds(animals)

# class Duck:
#     def quack(self):
#         print("Quack, quack!")

# class Person:
#     def quack(self):
#         print("I'm Quacking Like a Duck!")

# def make_it_quack(duck):
#     duck.quack()

# duck = Duck()
# person = Person()

# make_it_quack(duck)
# make_it_quack(person)

# class Dog:
#     def speak(self) -> str:
#         return "Woof"

# class Cat:
#     def speak(self) -> str:
#         return "Meow"

# class Robot:
#     def speak(self) -> str:
#         return "Beep boop"

# def make_it_speak(speaker) -> None:
#     print(speaker.speak())

# dog = Dog()
# cat = Cat()
# robot = Robot()

# make_it_speak(dog)  # Виведе: Woof
# make_it_speak(cat)  # Виведе: Meow
# make_it_speak(robot)  # Виведе: Beep boop

# from collections import UserDict

# class MyDictionary(UserDict):
#     # Приклад додавання нового методу
#     def add_key(self, key, value):
#         self.data[key] = value

# # Створення екземпляра власного класу
# my_dict = MyDictionary({'a': 1, 'b': 2})
# my_dict.add_key('c', 3)
# print(my_dict)

# from collections import UserDict

# contacts = [
#     {
#         "name": "Allen Raymond",
#         "email": "nulla.ante@vestibul.co.uk",
#         "phone": "(992) 914-3792",
#         "favorite": False,
#     },
#     {
#         "name": "Chaim Lewis",
#         "email": "dui.in@egetlacus.ca",
#         "phone": "(294) 840-6685",
#         "favorite": False,
#     },
#     {
#         "name": "Kennedy Lane",
#         "email": "mattis.Cras@nonenimMauris.net",
#         "phone": "(542) 451-7038",
#         "favorite": True,
#     }
# ]

# class Customer(UserDict):
#     def phone_info(self):
#         return f"{self.get('name')}: {self.get('phone')}"

#     def email_info(self):
#         return f"{self.get('name')}: {self.get('email')}"

# if __name__ == "__main__":
#     customers = [Customer(el) for el in contacts]

#     print("---------------------------")

#     for customer in customers:
#         print(customer.phone_info())

#     print("---------------------------")

#     for customer in customers:
#         print(customer.email_info())

# from collections import UserList

# class MyList(UserList):
#     # Додавання спеціалізованої поведінки. Наприклад, метод для додавання елемента, якщо він ще не існує
#     def add_if_not_exists(self, item):
#         if item not in self.data:
#             self.data.append(item)

# # Створення екземпляру MyList
# my_list = MyList([1, 2, 3])
# print("Оригінальний список:", my_list)

# # Додавання елементу, якщо він не існує
# my_list.add_if_not_exists(3)  # Не додасться, бо вже існує
# my_list.add_if_not_exists(4)  # Додасться, бо ще не існує
# print("Оновлений список:", my_list)

# from collections import UserList

# class CountableList(UserList):
#     def sum(self):
#         return sum(map(lambda x: int(x), self.data))

# countable = CountableList([1, '2', 3, '4'])
# countable.append('5')
# print(countable.sum())

# from collections import UserString

# class TruncatedString(UserString):
#     MAX_LEN = 7

#     def truncate(self):
#         self.data = self.data[:self.MAX_LEN]

# ts = TruncatedString('hello world!')
# ts.truncate()
# print(ts)

# from dataclasses import dataclass

# @dataclass
# class Rectangle:
#     width: int
#     height: int

#     def area(self) -> int:
#         return self.width * self.height

# rect1 = Rectangle(10, 5)
# rect2 = Rectangle(7, 3)
# rect3 = Rectangle(8, 6)

# print(f"Площа прямокутника 1: {rect1.area()}")
# print(f"Площа прямокутника 2: {rect2.area()}")
# print(f"Площа прямокутника 3: {rect3.area()}")

# from enum import Enum, auto

# class OrderStatus(Enum):
#     NEW = auto()
#     PROCESSING = auto()
#     SHIPPED = auto()
#     DELIVERED = auto()

# class Order:
#     def __init__(self, name: str, status: OrderStatus):
#         self.name = name
#         self.status = status

#     def update_status(self, new_status: OrderStatus):
#         self.status = new_status
#         print(f"Замовлення '{self.name}' оновлено до статусу {self.status.name}.")

#     def display_status(self):
#         print(f"Статус замовлення '{self.name}': {self.status.name}.")

# order1 = Order("Ноутбук", OrderStatus.NEW)
# order2 = Order("Книга", OrderStatus.NEW)

# order1.display_status()
# order2.display_status()

# order1.update_status(OrderStatus.PROCESSING)
# order2.update_status(OrderStatus.SHIPPED)

# order1.display_status()
# order2.display_status()

# class Owner:
#     def __init__(self, name, phone):
#         self.name = name
#         self.phone = phone

#     def info(self):
#         return f"{self.name}: {self.phone}"

# class Cat(Owner):
#     def __init__(self, nickname, age, name, phone):
#         super().__init__(name, phone)
#         self.nickname = nickname
#         self.age = age

#     def cat_info(self):
#         return f"Cat Name: {self.nickname}, Age: {self.age}"

# 	def sound(self):
# 	    return "Meow"

# cat = Cat('Simon', 4, 'Boris', '+380503002010')
# print(cat.info())
# print(cat.cat_info())

class Task:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def display_info(self):
        print(f"Задача: {self.name}, Опис: {self.description}")

class Project:
    def __init__(self, name: str):
        self.name = name
        self.tasks: list(Task) = []

    def add_task(self, name: str, description: str):
        self.tasks.append(Task(name, description))

    def remove_task(self, name: str):
        self.tasks = [task for task in self.tasks if task.name != name]

    def display_project_info(self):
        print(f"Проект: {self.name}")
        for task in self.tasks:
            task.display_info()

# Створення проекту
my_project = Project("Веб-розробка")

# Додавання задач
my_project.add_task("Дизайн інтерфейсу", "Створити макет головної сторінки.")
my_project.add_task("Розробка API", "Реалізувати ендпоінти для користувачів.")

# Відображення інформації про проект
my_project.display_project_info()

# Видалення задачі
my_project.remove_task("Розробка API")

# Перевірка видалення задачі
my_project.display_project_info()

# Визначення власного класу винятку
class AgeVerificationError(Exception):
    def __init__(self, message="Вік не задовольняє мінімальній вимозі"):
        self.message = message
        super().__init__(self.message)

# Функція для перевірки віку
def verify_age(age: int):
    if age < 18:
        raise AgeVerificationError("Вік особи меньший за 18 років")

if __name__ == "__main__":
    # Обробка винятку
    try:
        verify_age(16)  # Змініть вік для різних результатів
    except AgeVerificationError as e:
        print(f"Виняток: {e}")
    else:
        print("Вік перевірено, особа доросла.")
