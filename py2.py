# ім_я = input("Введіть ваше ім'я: ")

# вітання = f"Привіт, {ім_я}!"

# print(вітання)


rate = 1.68
value_day = 15
value_night = 10
payment = (rate * value_day) + ((rate / 2) *value_night)
# print(payment)


first_name = "Vlad"
last_name = "P"
full_name = f"{first_name} {last_name}"
# print(full_name)


length = "2.75"
width = "1.75"
area = float(length) * float(width)
show = f"With width {width} and length {length} of the room, its area is equal to {area:.2f}"
# print(show)


# name = input("Your name? ")
# email = input("Your email? ")
# age = int(input("Your age? "))
# height = float(input("Your height? "))
# is_active = True
# print(name, email, age, height, is_active)


my_list = []
my_list.insert(0, 2024)
my_list.insert(1, "Python")
my_list.insert(2, 3.12)
# print(my_list)


my_list = [2024, 3.12]
some_data = ['Python']
my_list.extend(some_data)
my_list.insert(1, "Python")
my_list.reverse()
# print(my_list)


data = {}
data.update({"year": 2024, "lang": "Python", "version": 3.12})
# print(data)


cat = {}
info = {"status": "vaccinated", "breed": True}
cat.update({"nick": "Simon", "age": 7, "characteristics": ["лагідний", "кусається"]})
age = cat.get("age")
cat.update(info)
# print(cat)