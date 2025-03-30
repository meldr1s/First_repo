import random

max = 49
min = 1
quantity = 6
def get_numbers_ticket(min, max, quantity):
    random_tickets = random.sample(range(min, max+1), quantity)
    return random_tickets
random_tickets = get_numbers_ticket(min, max, quantity)
print(random_tickets)