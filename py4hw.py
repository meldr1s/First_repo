# def total_salary(path):
#     try:
#         total = 0
#         count = 0
        
#         with open(path, 'r', encoding='utf-8') as file:
#             for line in file:
#                 try:
#                     name, salary = line.strip().split(',')
#                     total += int(salary)
#                     count += 1
#                 except ValueError:
#                     print(f"Невірний формат даних у рядку: {line}")
        
#         if count > 0:
#             average_salary = total / count
#         else:
#             average_salary = 0
        
#         return (total, average_salary)

#     except FileNotFoundError:
#         print(f"Файл за шляхом {path} не знайдено.")
#         return (0, 0)


# total, average = total_salary(r"C:\Users\ADMIN\Downloads\python\First_repo\path.txt")
# print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


# def get_cats_info(path):
#     cats_info = []

#     try:
#         with open(path, 'r', encoding='utf-8') as file:
#             for line in file:
#                 try:
#                     cat_id, name, age = line.strip().split(',')
#                     cats_info.append({
#                         "id": cat_id,
#                         "name": name,
#                         "age": age
#                     })
#                 except ValueError:
#                     print(f"Невірний формат даних у рядку: {line}")
        
#         return cats_info

#     except FileNotFoundError:
#         print(f"Файл за шляхом {path} не знайдено.")
#         return []
        
# cats_info = get_cats_info(r"C:\Users\ADMIN\Downloads\python\First_repo\path.txt")
# print(cats_info)


# import os
# import sys
# from colorama import Fore, init

# init(autoreset=True)

# def list_directory_structure(path):
#     try:
#         if not os.path.isdir(path):
#             print(f"{Fore.RED}Шлях {path} не є директорією або не існує.")
#             return

#         for root, dirs, files in os.walk(path):
#             for dir_name in dirs:
#                 print(f"{Fore.BLUE}{dir_name}")
#             for file_name in files:
#                 print(f"{Fore.GREEN}{file_name}")

#     except Exception as e:
#         print(f"{Fore.RED}Помилка: {e}")

# if len(sys.argv) != 2:
#     print(f"{Fore.RED}Будь ласка, вкажіть шлях до директорії як аргумент командного рядка.")
# else:
#     path = sys.argv[1]
#     list_directory_structure(path)


