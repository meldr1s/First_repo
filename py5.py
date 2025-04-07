# from collections import namedtuple

# # Створення іменованого кортежу
# Point = namedtuple('Point', ['x', 'y'])

# p = Point(11, y=22)

# # Доступ до елементів
# print(p.x)  # 11
# print(p.y)  # 22

# import collections

# person = ('Mick', 'Nitch', 35, 'Boston', '01146')
# Person = collections.namedtuple('Person', ['first_name', 'last_name', 'age', 'birth_place', 'post_index'])

# # Створення екземпляра Person
# person = Person('Mick', 'Nitch', 35, 'Boston', '01146')

# # Виведення різних атрибутів іменованого кортежу
# print(person.first_name)
# print(person.post_index)
# print(person.age)
# print(person[3])

# Cat = collections.namedtuple('Cat', ['nickname', 'age', 'owner'])

# cat = Cat('Simon', 4, 'Krabat')

# print(f'This is a cat {cat.nickname}, {cat.age} age, his owner {cat.owner}')

# print(f'This is a cat {cat[0]}, {cat[1]} age, his owner {cat[2]}')

# import collections

# student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
# mark_counts = {}
# for mark in student_marks:
#     if mark in mark_counts:
#         mark_counts[mark] += 1
#     else:
#         mark_counts[mark] = 1

# print(mark_counts)

# student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7 , 1, 1, 1, 3, 5]
# mark_counts = collections.Counter(student_marks)
# print(mark_counts)
# print(mark_counts.most_common())
# print(mark_counts.most_common(1))
# print(mark_counts.most_common(2))

# from collections import Counter

# letter_count = Counter("banana")
# print(letter_count)

# sentence = "the quick brown fox jumps over the lazy dog"
# words = sentence.split()
# word_count = Counter(words)

# # Виведення слова та його частоти
# for word, count in word_count.items():
#     print(f"{word}: {count}")

# from collections import defaultdict

# # Створення defaultdict з list як фабрикою за замовчуванням
# d = defaultdict(list)

# # Додавання елементів до списку для кожного ключа
# d['a'].append(1)
# d['a'].append(2)
# d['b'].append(4)

# print(d)

# d = defaultdict(int)

# # Збільшення значення для кожного ключа
# d['a'] += 1
# d['b'] += 1
# d['a'] += 1

# print(d)

# from collections import defaultdict

# words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
# grouped_words = {}

# for word in words:
#     char = word[0]
#     if char not in grouped_words:
#         grouped_words[char] = []
#     grouped_words[char].append(word)

# print(grouped_words)

# if char not in grouped_words:
#     grouped_words[char] = []

# from collections import defaultdict

# words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
# grouped_words = defaultdict(list)

# for word in words:
#     char = word[0]
#     grouped_words[char].append(word)

# print(dict(grouped_words))

# # Створення стеку
# def create_stack():
#     return []

# # Перевірка на порожнечу
# def is_empty(stack):
#     return len(stack) == 0

# # Додавання елементу
# def push(stack, item):
#     stack.append(item)

# # Вилучення елементу
# def pop(stack):
#     if not is_empty(stack):
#         return stack.pop()
#     else:
#         print("Стек порожній")

# # Перегляд верхнього елемента
# def peek(stack):
#     if not is_empty(stack):
#         return stack[-1]
#     else:
#         print("Стек порожній")

# stack = create_stack()
# push(stack, 'a')
# push(stack, 'b')
# push(stack, 'c')

# print(peek(stack))

# from collections import deque

# # Створення черги
# queue = deque()

# # Enqueue: Додавання елементів
# queue.append('a')
# queue.append('b')
# queue.append('c')

# print("Черга після додавання елементів:", list(queue))

# # Dequeue: Видалення елемента
# print("Видалений елемент:", queue.popleft())

# print("Черга після видалення елемента:", list(queue))

# # Peek: Перегляд першого елемента
# print("Перший елемент у черзі:", queue[0])

# # IsEmpty: Перевірка на порожнечу
# print("Чи черга порожня:", len(queue) == 0)

# # Size: Розмір черги
# print("Розмір черги:", len(queue))

# from collections import deque

# # Створення пустої двосторонньої черги
# d = deque()

# # Додаємо елементи в чергу
# d.append('middle')  # Додаємо 'middle' в кінець черги
# d.append('last')    # Додаємо 'last' в кінець черги
# d.appendleft('first')  # Додаємо 'first' на початок черги

# # Виведення поточного стану черги
# print("Черга після додавання елементів:", list(d))

# # Видалення та виведення останнього елемента (з правого кінця)
# print("Видалений останній елемент:", d.pop())

# # Видалення та виведення першого елемента (з лівого кінця)
# print("Видалений перший елемент:", d.popleft())

# # Виведення поточного стану черги після видалення елементів
# print("Черга після видалення елементів:", list(d))

# from collections import deque

# d = deque(maxlen=5)
# for i in range(10):
#     d.append(i)

# print(d)

# from collections import deque

# # Список завдань, де кожне завдання - це словник
# tasks = [
#     {"type": "fast", "name": "Помити посуд"},
#     {"type": "slow", "name": "Подивитись серіал"},
#     {"type": "fast", "name": "Вигуляти собаку"},
#     {"type": "slow", "name": "Почитати книгу"}
# ]

# # Ініціалізація черги завдань
# task_queue = deque()

# # Розподіл завдань у чергу відповідно до їх пріоритету
# for task in tasks:
#     if task["type"] == "fast":
#         task_queue.appendleft(task)  # Додавання на високий пріоритет
#         print(f"Додано швидке завдання: {task['name']}")
#     else:
#         task_queue.append(task)  # Додавання на низький пріоритет
#         print(f"Додано повільне завдання: {task['name']}")

# # Виконання завдань
# while task_queue:
#     task = task_queue.popleft()
#     print(f"Виконується завдання: {task['name']}")

# from decimal import Decimal

# print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))
# print(Decimal("0.1") + Decimal("0.2"))

# from decimal import Decimal, getcontext

# getcontext().prec = 6
# print(Decimal("1") / Decimal("7"))

# getcontext().prec = 8
# print(Decimal("1") / Decimal("7"))

# from decimal import Decimal, getcontext

# getcontext().prec = 6
# print(Decimal("233") / Decimal("7"))

# from decimal import Decimal, ROUND_DOWN

# # Вихідне число Decimal
# number = Decimal('3.14159')

# # Встановлення точності до двох знаків після коми
# rounded_number = number.quantize(Decimal('0.00'), rounding=ROUND_DOWN)

# print(rounded_number)

# import decimal
# from decimal import Decimal
 
# number = Decimal("1.45")

# # Округлення за замовчуванням до одного десяткового знаку
# print("Округлення за замовчуванням ROUND_HALF_EVEN:", number.quantize(Decimal("0.0")))

# # Округлення вверх при нічиї (ROUND_HALF_UP)
# print("Округлення вгору ROUND_HALF_UP:", number.quantize(Decimal("0.0"), rounding=decimal.ROUND_HALF_UP))

# # Округлення вниз (ROUND_FLOOR)
# print("Округлення вниз ROUND_FLOOR:", number.quantize(Decimal("0.0"), rounding=decimal.ROUND_FLOOR))

# # Округлення вверх (ROUND_CEILING)
# print("Округлення вгору ROUND_CEILING:", number.quantize(Decimal("0.0"), rounding=decimal.ROUND_CEILING))

# # Округлення до трьох десяткових знаків за замовчуванням
# print("Округлення до трьох десяткових знаків:", Decimal("3.14159").quantize(Decimal("0.000")))

# def my_generator():
#     yield 1
#     yield 2
#     yield 3

# gen = my_generator()

# # Використання next()
# print(next(gen))  # Виведе 1
# print(next(gen))  # Виведе 2
# print(next(gen))  # Виведе 3

# def count_down(start):
#     while start > 0:
#         yield start
#         start -= 1

# for number in count_down(5):
#     print(number)

# def read_lines(file_path):
#     with open(file_path, 'r', encoding="utf-8") as file:
#         for line in file:
#             yield line.strip()

# # Використання генератора для читання рядків з файлу
# for line in read_lines("my_file.txt"):
#     print(line)

# def my_function():
#     print("Hello, world!")

# f = my_function
# f()

# from typing import Callable

# def add(a: int, b: int) -> int:
#     return a + b

# def multiply(a: int, b: int) -> int:
#     return a * b

# def apply_operation(a: int, b: int, operation: Callable[[int, int], int]) -> int:
#     return operation(a, b)

# # Використання
# result_add = apply_operation(5, 3, add)
# result_multiply = apply_operation(5, 3, multiply)

# print(result_add, result_multiply)

# from typing import Callable

# def power(exponent: int) -> Callable[[int], int]:
#     def inner(base: int) -> int:
#         return base ** exponent
#     return inner

# # Використання
# square = power(2)
# cube = power(3)

# print(square(4)) 
# print(cube(4))

# from typing import Callable, Dict

# # Визначення функцій
# def add(a: int, b: int) -> int:
#     return a + b

# def multiply(a: int, b: int) -> int:
#     return a * b

# def power(exponent: int) -> Callable[[int], int]:
#     def inner(base: int) -> int:
#         return base ** exponent
#     return inner

# # Використання power для створення функцій square та cube
# square = power(2)
# cube = power(3)

# # Словник операцій
# operations: Dict[str, Callable] = {
#     'add': add,
#     'multiply': multiply,
#     'square': square,
#     'cube': cube
# }

# # Використання операцій
# result_add = operations['add'](10, 20)  # 30
# result_square = operations['square'](5)  # 25

# print(result_add)  
# print(result_square)  

# def outer_function(msg):
#     message = msg

#     def inner_function():
#         print(message)

#     return inner_function

# # Створення замикання
# my_func = outer_function("Hello, world!")
# my_func()

# from typing import Callable

# def counter() -> Callable[[], int]:
#     count = 0

#     def increment() -> int:
#         # використовуємо nonlocal, щоб змінити змінну в замиканні
#         nonlocal count  
#         count += 1
#         return count

#     return increment

# # Створення лічильника
# count_calls = counter()

# # Виклики лічильника
# print(count_calls())  # Виведе 1
# print(count_calls())  # Виведе 2
# print(count_calls())  # Виведе 3

# def add(a):
#     def add_b(b):
#         return a + b
#     return add_b

# # Використання:
# add_5 = add(5)
# result = add_5(10)
# print(result)

# def apply_discount(price: float, discount_percentage: int) -> float:
#     return price * (1 - discount_percentage / 100)

# # Використання
# discounted_price = apply_discount(500, 10)  # Знижка 10% на ціну 500
# print(discounted_price)

# discounted_price = apply_discount(500, 20)  # Знижка 20% на ціну 500
# print(discounted_price)

# from typing import Callable

# def discount(discount_percentage: int) -> Callable[[float], float]:
#     def apply_discount(price: float) -> float:
#         return price * (1 - discount_percentage / 100)
#     return apply_discount

# # Каррінг в дії
# ten_percent_discount = discount(10)
# twenty_percent_discount = discount(20)

# # Застосування знижок
# discounted_price = ten_percent_discount(500)  # 450.0
# print(discounted_price)

# discounted_price = twenty_percent_discount(500)  # 400.0
# print(discounted_price)

# from typing import Callable, Dict

# def discount(discount_percentage: int) -> Callable[[float], float]:
#     def apply_discount(price: float) -> float:
#         return price * (1 - discount_percentage / 100)
#     return apply_discount

# # Створення словника з функціями знижок
# discount_functions: Dict[str, Callable] = {
#     "10%": discount(10),
#     "20%": discount(20),
#     "30%": discount(30)
# }

# # Використання функції зі словника
# price = 500
# discount_type = "20%"

# discounted_price = discount_functions[discount_type](price)
# print(f"Ціна зі знижкою {discount_type}: {discounted_price}")

# def complicated(x: int, y: int) -> int:
#     return x + y

# def logger(func):
#     def inner(x: int, y: int) -> int:
#         print(f"Викликається функція: {func.__name__}: {x}, {y}")
#         result = func(x, y)
#         print(f"Функція {func.__name__} завершила виконання: {result}")
#         return result

#     return inner

# complicated = logger(complicated)
# print(complicated(2, 3))

# def logger(func):
#     def inner(x: int, y: int) -> int:
#         print(f"Викликається функція: {func.__name__}: {x}, {y}")
#         result = func(x, y)
#         print(f"Функція {func.__name__} завершила виконання: {result}")
#         return result

#     return inner

# @logger
# def complicated(x: int, y: int) -> int:
#     return x + y

# print(complicated(2, 3))

# from functools import wraps

# def logger(func):
#     @wraps(func)
#     def inner(x: int, y: int) -> int:
#         print(f"Викликається функція: {func.__name__}: {x}, {y}")
#         result = func(x, y)
#         print(f"Функція {func.__name__} завершила виконання: {result}")
#         return result

#     return inner

# @logger
# def complicated(x: int, y: int) -> int:
#     return x + y

# print(complicated(2, 3))
# print(complicated.__name__)

# sq = []
# for i in range(1, 6):
#     sq.append(i**2)

# print(sq)

# even_squares = []
# for x in range(1, 10):
#     if x % 2 == 0:
#         even_squares.append(x**2)

# print(even_squares)  # Виведе [4, 16, 36, 64]

# add = lambda x, y: x + y
# print(add(5, 3))  # Виведе 8

# nums = [1, 2, 3, 4, 5]
# nums_sorted = sorted(nums, key=lambda x: -x)
# print(nums_sorted)

# def is_positive(x):
#     return x > 0

# nums = [-2, -1, 0, 1, 2]
# positive_nums = filter(is_positive, nums)

# print(list(positive_nums))

# some_str = 'Видавництво А-БА-БА-ГА-ЛА-МА-ГА'

# new_str = ''.join(list(filter(lambda x: x.islower(), some_str)))
# print(new_str)

# nums = [1, 2, 3, 4, 5, 6]
# even_nums = [x for x in nums if x % 2 == 0]
# print(even_nums)

nums = [0, False, 5, 0]
result = any(nums)  
print(result)

nums = [1, 3, 5, 7, 9]
result = any(x % 2 == 0 for x in nums)  
print(result)

nums = [1, 2, 3, 4]
result = all(nums)  
print(result)

nums = [1, 2, 3, 4]
is_all_even = all(x % 2 == 0 for x in nums) 
print(is_all_even)

words = ["Hello", "World", "Python"]
is_all_title_case = all(word.istitle() for word in words)
print(is_all_title_case)
