from datetime import datetime
import random, re

# date = str(input("Введіть дату (РРРР-ММ-ДД): "))
date = "2021-10-09"

def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        delta = (today - input_date).days
        if "-" in str(delta):
            delta = str(delta).replace("-", "")
            print(f"До цієї дати {delta} днів.")
        else:
            print(f"Ця дата була {delta} днів назад.")
    except:
        print("Введіть дату в форматі (РРРР-ММ-ДД)")
# get_days_from_today(date)



max = 49
min = 1
quantity = 6
def get_numbers_ticket(min, max, quantity):
    random_tickets = random.sample(range(min, max+1), quantity)
    return random_tickets
# random_tickets = get_numbers_ticket(min, max, quantity)
# print(random_tickets)



phone_number = [
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   " 
]

def normalize_phone(phone_numbers):
    n_numbers = []
    for phone in phone_numbers:
        phone = re.sub(r"[^\d]", "", phone)
        if phone.startswith("380"):
            n_numbers.append("+" + phone)
        else:
            n_numbers.append("+380" + phone.lstrip("0"))
    return n_numbers

true_n = normalize_phone(phone_number)

for number in true_n:
    print(number)

