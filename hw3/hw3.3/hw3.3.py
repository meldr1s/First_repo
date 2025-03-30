import re

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