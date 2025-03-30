from datetime import datetime

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
get_days_from_today(date)