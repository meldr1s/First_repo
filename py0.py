name = "vlad"
age = 27
weight = 90.1
is_student = False
# print(name, age, weight, is_student)


languages = ["Python", "Java", "JavaScript"]
languages.insert(2, "C++")
# print(languages)
languages.remove("Java")
# print(languages)


language = {"name": "Python", "version": 3.11}
language["year"] = 1991
language["version"] = 3.12
# print(language)
del language["year"]
# print(language)


condition = 0

if condition == 0:
    value = 10
    # print("+")



condition = 7

if condition == 13:
    value = 10
    # print("-")
else:
    value = 20
    # print("+")


condition = 7

if condition >= 13:
    value = 10
    # print("1")
elif condition >= 1:
    value = 15
    # print("2")
else:
    value = 20
    # print("3")


languages = ["Python", "Java", "C++", "JavaScript"]
# for language in languages:
    # print(language)


see = "The quick brown fox jumps over the lazy dog"
length = 0
for i in see:
    if i != " ":
        length = length + 1
        # print(length)


summary = 0

for i in range(1, 101):
    summary = summary + i
    # print(summary)


N = 10
sum_squares = 0
i = 1
while i <=N:
    sum_squares += i * i
    i += 1

# print(f"The sum of the squares of numbers from 1 to {N} is {sum_squares}")


def function(): 
    print("Hello world!")
# function()


message = "Hello world!"
def function(message):
    print(message)
# function(message)


N = 10

def function(n):
    sum_squares = 0
    i = 1
    while i <= n:
        sum_squares += i * i  
        i += 1  
    return sum_squares  

result = function(N)  
# print(f"The sum of the squares of numbers from 1 to {N} is {result}")


first_name = "John"
last_name = "Doe"


def get_fullname(first_name, last_name):
    full = first_name + " " + last_name
    return full

fullname = get_fullname(first_name, last_name)
# print(fullname)


first_name = "John"
last_name = "Doe"


def get_initials(first_name, last_name):
    name = str(last_name) + " " + first_name[0] + "."
    return name

formatted_name  = get_initials(first_name, last_name)
# print(formatted_name)


first = "Python"
second = "python"


def compare(first, second):
    if first.upper() == second.upper():
        return True
    else:
        return False
    


result = compare(first, second)
# print(result)


text = "Hello, world! Welcome to the world of Python."

position = text.find("world")
# print(position)

updated_text = text.replace("world", "planet")
# print(updated_text)


product_name = "Coffee Maker"
product_price = 7500.50
product_quantity = 15


def format_product_info(product_name, product_price, product_quantity):
    coffe = f"Product: {product_name}, Price: {product_price} UAH, Quantity: {product_quantity} pcs."
    return coffe

product_info = format_product_info(product_name, product_price, product_quantity)
# print(product_info)


class Car:
    vehicle_type = "Automobile"

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.year} {self.make} {self.model}, Type: {Car.vehicle_type}"
    
car_ford = Car("Ford", "Mustang", 2022)
car_toyota = Car("Toyota", "Corolla", 2021)
print(car_ford.get_info())
print(car_toyota.get_info())

