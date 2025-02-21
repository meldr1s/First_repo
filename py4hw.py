def total_salary(path):
    def total_salary(path):
    try:
        total = 0
        count = 0
        
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    name, salary = line.strip().split(',')
                    total += int(salary)
                    count += 1
                except ValueError:
                    print(f"Невірний формат даних у рядку: {line}")
        
        if count > 0:
            average_salary = total / count
        else:
            average_salary = 0
        
        return (total, average_salary)

    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return (0, 0)

path = 'path.txt'
result = total_salary(path)
print(f"Загальна сума: {result[0]}, Середня зарплата: {result[1]}")
