# name = "Taras"
# age = 22
# has_driver_licence = True

# if name and age >= 18 and has_driver_licence:
#     print(f"User {name} can rent a car")


# num = int(input("Введіть число: "))

# length = len(str(num))

# if length == 2 and num % 2 == 0:
#     print("Парне двозначне число")
# else:
#     print("Ні")


# is_next = None
# num = int(input("Enter the number of points: "))
# if num >= 83:
#     is_next = True
#     print("True")
# else:
#     is_next = False
#     print("False")


# work_experience = int(input("Enter your full work experience in years: "))
# developer_type = None
# if work_experience > 1 and work_experience <= 5:
#     developer_type = "Middle"
# elif work_experience <= 1:
#     developer_type = "Junior"
# else:
#     developer_type = "Senior"
# print(developer_type)


# num = int(input("Enter a number: "))
# result = None
# if num > 0:
#     if num % 2 == 1:
#         result = "Positive odd number"
#     else:
#         result = "Positive even number"
# elif num < 0:
#     result = "Negative number"
# else:
#     result = "It is zero"
# print(result)


# num = int(input("Enter the integer (0 to 100): "))
# sum = 0

# if num < 0 or num > 100:
#     print("Incorrect number")
# else:
#     while num > 0:
#         sum += num
#         num -= 1
# print(sum)


# message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
# search = "r"
# result = 0
# for m in message:
#     if m == search:
#         result += 1
# print(result)


# pool = 1000
# quantity = int(input("Enter the number of mailings: "))
# try:
#     chunk = pool // quantity
#     print(f"Each mailing will have {chunk} SMS.")
# except ZeroDivisionError:
#     print('Divide by zero completed!')


# def greeting():
#     print("Hello world!")
# greeting()

# username = str(input("Your username :"))
# def invite_to_event(username):
#     invite = f"Dear {username}, we have the honour to invite you to our event"
#     return invite
# invite = invite_to_event(username)
# print(invite)


# price = 100
# discount = 0.1

# def discount_price(price, discount):
#     def apply_discount(discount):
#         nonlocal price 
#         price = price * (1 - discount)
#         print(price)
#         return price
#     apply_discount(discount)
#     return price
# discount_price(price, discount)
# print(price)


# first_name = "V"
# last_name = "P"
# middle_name = ""
# def get_fullname(first_name, last_name, middle_name=""):
#     if middle_name:
#         return f"Ваше імя {first_name} {middle_name} {last_name}."
#     else:
#         return f"Ваше імя {first_name} {last_name}."
# fullname = get_fullname(first_name, last_name, middle_name)
# print(fullname)


# string = "123   "
# length = 20
# def format_string(string, length):
#     if len(string) >= length:
#         return string
#     else:
#         strlen = " " * ((length - len(string)) // 2)
#         return strlen + string
# newstring = format_string(string, length)
# print(newstring)


# def first(size, *args):
#     return size + len(args)

# def second(size, **kwargs):
#     return size + len(kwargs)

# print(first(5, "first", "second", "third"))
# print(first(1, "Alex", "Boris"))
# print(second(3, comment_one="first", comment_two="second", comment_third="third"))
# print(second(10, comment_one="Alex", comment_two="Boris"))


# def factorial(n):
#     if n < 2:
#         return 1
#     else:
#         return n * factorial(n - 1)

# def number_of_groups(n, k):
#     return factorial(n) // (factorial(n - k) * factorial(k))
