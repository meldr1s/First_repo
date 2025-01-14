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
