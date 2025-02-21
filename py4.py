# fh = open('test_file.txt')

# fh = open('test.txt')
# # операції над файлом
# fh.close()

# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

# fh = open('test.txt', 'w')
# symbols_written = fh.write('hello!')
# print(symbols_written) # 6
# fh.close()

# fh = open('test.txt', 'w+')
# fh.write('hello!')
# fh.seek(0)

# first_two_symbols = fh.read(2)
# print(first_two_symbols)  # 'he'

# fh.close()

# fh = open('test.txt', 'w')
# fh.write('hola!')
# fh.close()

# fh = open('test.txt', 'r')
# all_file = fh.read()
# print(all_file)  # 'hello!'

# fh.close()

# fh = open('test.txt', 'w')
# fh.write('hello!')
# fh.close()

# fh = open('test.txt', 'r')
# while True:
#     symbol = fh.read(1)
#     if len(symbol) == 0:
#         break
#     print(symbol)

# fh.close()

# fh = open('test.txt', 'w')
# fh.write('first line\nsecond line\nthird line')
# fh.close()

# fh = open('test.txt', 'r')
# while True:
#     line = fh.readline()
#     if not line:
#         break
#     print(line)

# fh.close()

# fh = open('test.txt', 'w')
# fh.write('first line\nsecond line\nthird line')
# fh.close()

# fh = open('test.txt', 'r')
# lines = fh.readlines()
# print(lines)

# fh.close()

# fh = open("test.txt", "w")
# fh.write("first line\nsecond line\nthird line")
# fh.close()

# fh = open("test.txt", "r")
# lines = [el.strip() for el in fh.readlines()]
# print(lines)

# fh.close()

# fh = open('test.txt', 'w+')
# fh.write('hello!')

# fh.seek(1)
# second = fh.read(1)
# print(second)  # 'e'

# fh.close()

# fh = open("test.txt", "w+")
# fh.write("hello!")

# position = fh.tell()
# print(position)  # 6

# fh.seek(1)
# position = fh.tell()
# print(position)  # 1

# fh.read(2)
# position = fh.tell()
# print(position)  # 3

# fh.close()

# fh = open('text.txt', 'w')
# try:
#     # Виконання операцій з файлом
#     fh.write('Some data')
# finally:
#     # Закриття файлу в блоці finally гарантує, що файл закриється навіть у разі помилки
#     fh.close()

# with open('text.txt', 'w') as fh:
#     # Виконання операцій з файлом
#     fh.write('Some data')
# # Файл автоматично закриється після виходу з блоку with

# with open("test.txt", "w") as fh:
#     fh.write("first line\nsecond line\nthird line")

# with open("test.txt", "r") as fh:
#     lines = [el.strip() for el in fh.readlines()]

# print(lines)

# with open('raw_data.bin', 'wb') as fh:
#     fh.write(b'Hello world!')

# s = b'Hello!'
# print(s[1])  # Виведе: 101 (це ASCII-код символу 'e')

# byte_str = 'some text'.encode()
# print(byte_str)

# str.encode(encoding="utf-8", errors="strict")

# # Перетворення списку чисел у байт-рядок
# numbers = [0, 128, 255]
# byte_numbers = bytes(numbers)
# print(byte_numbers)  # Виведе байтове представлення чисел

# for num in [127, 255, 156]:
#   print(hex(num))

# s = "Привіт!"

# utf8 = s.encode()
# print(f"UTF-8: {utf8}")

# utf16 = s.encode("utf-16")
# print(f"UTF-16: {utf16}")

# cp1251 = s.encode("cp1251")
# print(f"CP-1251: {cp1251}")

# s_from_utf16 = utf16.decode("utf-16")
# print(s_from_utf16 == s)

# print(b'Hello world!'.decode('utf-16'))

# # Відкриття текстового файлу з явними вказівками UTF-8 кодування
# with open('example.txt', 'r', encoding='utf-8') as file:
#     content = file.read()
#     print(content)

# byte_array = bytearray(b'Kill Bill')
# byte_array[0] = ord('B')
# byte_array[5] = ord('K')
# print(byte_array)

# byte_array = bytearray(b"Hello")
# byte_array.append(ord("!"))  
# print(byte_array)

# byte_array = bytearray(b"Hello World")
# string = byte_array.decode("utf-8")
# print(string)  # Виведе: 'Hello World'

# string1 = "Hello World"
# string2 = "hello world"
# if string1.lower() == string2.lower():
#     print("Рядки однакові")
# else:
#     print("Рядки різні")

# text = "Python Programming"
# print(text.casefold())

# german_word = 'straße'  # В нижньому регістрі
# search_word = 'STRASSE'  # В верхньому регістрі

# # Порівняння за допомогою lower()
# lower_comparison = german_word.lower() == search_word.lower()

# # Порівняння за допомогою casefold()
# casefold_comparison = german_word.casefold() == search_word.casefold()

# print(f"Порівняння з lower(): {lower_comparison}")
# print(f"Порівняння з casefold(): {casefold_comparison}")

# shutil.make_archive(base_name, format, root_dir=None, base_dir=None)

# import shutil

# # Створення ZIP-архіву з вмістом директорії 'my_folder'
# shutil.make_archive('example', 'zip', root_dir='my_folder')

# shutil.unpack_archive(filename, extract_dir=None, format=None)

# import shutil

# # Розпакування ZIP-архіву в певну директорію
# shutil.unpack_archive('example.zip', 'destination_folder')

# import shutil

# # Копіюємо файл
# source_file = '/path/to/source/file.txt'
# destination_dir = '/path/to/destination'
# shutil.copy(source_file, destination_dir)

# # Копіюємо всю директорію
# source_dir = '/path/to/source/directory'
# destination_dir = '/path/to/destination/directory'
# shutil.copytree(source_dir, destination_dir)

# from pathlib import PurePath

# p = PurePath("/usr/bin/simple.jpg")
# print("Name:", p.name)  
# print("Suffix:", p.suffix) 
# print("Parent:", p.parent)

# from pathlib import Path

# p = Path("example.txt")
# p.write_text("Hello, world!")
# print(p.read_text()) 
# print("Exists:", p.exists()) 

# from pathlib import Path

# # Для Unix/Linux
# path_unix = Path("/usr/bin/python3")

# # Для Windows
# path_windows = Path("C:/Users/ADNIN/Documents/file.txt")

# from pathlib import Path

# # Початковий шлях
# base_path = Path("/usr/bin")

# # Додавання додаткових частин до шляху
# full_path = base_path / "subdir" / "script.py"

# print(full_path)  # Виведе: /usr/bin/subdir/script.py

# from pathlib import Path

# # Перетворення відносного шляху в абсолютний
# relative_path = Path("documents/example.txt")
# absolute_path = relative_path.absolute()
# print(absolute_path)

# from pathlib import Path

# # Перетворення відносного шляху в абсолютний
# relative_path = Path("documents/example.txt")
# absolute_path = relative_path.absolute()

# current_working_directory = Path("E:\WebDir\Works\Python\python-help-solution\example_for_new_core\l04")
# relative_path = absolute_path.relative_to(current_working_directory)
# print(relative_path)

# from pathlib import Path

# # Початковий шлях до файлу
# original_path = Path("documents/example.txt")

# # Зміна імені файлу
# new_path = original_path.with_name("report.txt")
# print(new_path)

# from pathlib import Path

# # Початковий шлях до файлу
# original_path = Path("documents/example.txt")

# # Зміна імені файлу
# new_path = original_path.with_suffix(".md")
# print(new_path)

# from pathlib import Path

# original_path = Path("documents/example.txt")

# # Створює новий об'єкт Path з іншим ім'ям файлу
# new_path = original_path.with_name("report.txt")

# print(original_path)
# print(new_path)

# from pathlib import Path

# original_path = Path("documents/example.txt")

# # Створює новий об'єкт Path з іншим ім'ям файлу
# new_path = original_path.with_name("report.txt")
# original_path.rename(new_path)

# from pathlib import Path

# # Створення об'єкту Path для файлу
# file_path = Path("example.txt")

# # Запис тексту у файл
# file_path.write_text("Привіт світ!", encoding="utf-8")

# from pathlib import Path

# # Створення об'єкту Path для файлу
# file_path = Path("example.txt")

# # Читання тексту з файлу
# text = file_path.read_text(encoding="utf-8")
# print(text)

# from pathlib import Path

# # Створення об'єкту Path для бінарного файлу
# file_path = Path("example.bin")

# # Бінарні дані для запису
# data = b"Python is great!"

# # Запис байтів у файл
# file_path.write_bytes(data)

# from pathlib import Path

# # Створення об'єкту Path для бінарного файлу
# file_path = Path("example.bin")

# # Читання байтів з файлу
# binary_data = file_path.read_bytes()
# print(binary_data)

# from pathlib import Path

# # Створення об'єкту Path для директорії
# directory = Path("./picture")

# # Виведення переліку всіх файлів та піддиректорій
# for path in directory.iterdir():
#     print(path)

# from pathlib import Path
# directory = Path('/my_directory/new_folder')
# directory.mkdir(parents=True, exist_ok=True)

# from pathlib import Path
# directory = Path('/my_directory/new_folder')
# directory.rmdir()

# from pathlib import Path

# path = Path("./picture")

# # Перевірка існування
# if path.exists():
#     print(f"{path} існує")

# # Перевірка, чи це директорія
# if path.is_dir():
#     print(f"{path} є директорією")

# # Перевірка, чи це файл
# if path.is_file():
#     print(f"{path} є файлом")

# import shutil
# from pathlib import Path

# # Вихідний і цільовий файли
# source = Path('/path/to/source/file.txt')
# destination = Path('/path/to/destination/file.txt')

# # Копіювання файла
# shutil.copy(source, destination)

# import shutil
# from pathlib import Path

# # Вихідний і цільовий шляхи
# source = Path('/path/to/source/file.txt')
# destination = Path('/path/to/destination/file.txt')

# # Переміщення файла
# shutil.move(source, destination)

# from pathlib import Path

# file_path = Path("./picture/bot-icon.png")

# # Отримання розміру файла
# size = file_path.stat().st_size
# print(f"Розмір файла: {size} байтів")

# from pathlib import Path
# import time

# file_path = Path("./picture/bot-icon.png")

# # Час створення та модифікації
# creation_time = file_path.stat().st_ctime
# modification_time = file_path.stat().st_mtime

# print(f"Час створення: {time.ctime(creation_time)}")
# print(f"Час модифікації: {time.ctime(modification_time)}")

# from pathlib import Path

# # Створення об'єкту Path для файлу
# file_path = Path('/path/to/file.txt')

# # Перевірка, чи файл існує, перш ніж видаляти
# if file_path.exists():
#     file_path.unlink()
#     print(f'Файл {file_path} було видалено')
# else:
#     print(f'Файл {file_path} не існує')

# from pathlib import Path
# file_path = Path('/path/to/file.txt')
# file_path.unlink(missing_ok=True)

# import math

# sin_pi = math.sin(math.pi)

# from math import pi, sin

# sin_pi = sin(pi)

# # mymodule.py
# def say_hello(name):
#     return f"Hello, {name}!"

# # main.py
# import mymodule

# print(mymodule.say_hello("World"))

# # main.py
# from mymodule import say_hello

# print(say_hello("World"))

# # main.py
# from mymodule import say_hello as greeting

# print(greeting("World"))

# from module_name import item_name as alias

# # main.py
# from mymodule import say_hello as greeting

# print(dir())
# print(greeting("World"))

# def say_hello(name):
#     print(f'Hello, {name}')

# print("You imported hello.py")
# say_hello('user')
