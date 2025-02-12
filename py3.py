# import datetime
# print(datetime.datetime.now())

# from datetime import datetime
# current_datetime = datetime.now()
# print(current_datetime.year)
# print(current_datetime.month)
# print(current_datetime.day)
# print(current_datetime.hour)
# print(current_datetime.minute)
# print(current_datetime.second)
# print(current_datetime.microsecond)
# print(current_datetime.tzinfo)
# print(current_datetime.date())
# print(current_datetime.time())


# import datetime

# date_part = datetime.date(2023, 12, 14)
# time_part = datetime.time(12, 30, 15)
# specific_date = datetime.datetime(2020, 1, 7, 21, 32, 1)

# combined_datetime = datetime.datetime.combine(date_part, time_part)
# print(specific_date)
# print(combined_datetime)


# from datetime import datetime

# now = datetime.now()
# day_of_week = now.weekday()

# print(f"Сьогодні: {day_of_week}") 


# from datetime import timedelta
# delta = timedelta(
#     days=50,
#     seconds=27,
#     microseconds=10,
#     milliseconds=29000,
#     minutes=5,
#     hours=8,
#     weeks=2
# )
# print(delta)


# from datetime import datetime

# seventh_day_2019 = datetime(year=2019, month=1, day=7, hour=14)
# seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)

# difference = seventh_day_2020 - seventh_day_2019
# print(difference)  # 365 days, 0:00:00
# print(difference.total_seconds())  # 31536000.0


# from datetime import datetime, timedelta

# now = datetime.now()
# future_date = now + timedelta(days=10)  # Додаємо 10 днів до поточної дати
# print(future_date)


# from datetime import datetime, timedelta

# seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
# four_weeks_interval = timedelta(weeks=4)

# print(seventh_day_2020 + four_weeks_interval)  # 2020-02-04 14:00:00
# print(seventh_day_2020 - four_weeks_interval)  # 2019-12-10 14:00:00


# from datetime import datetime

# # Створення об'єкта datetime
# date = datetime(year=2023, month=12, day=18)

# # Отримання порядкового номера
# ordinal_number = date.toordinal()
# print(f"Порядковий номер дати {date} становить {ordinal_number}")


# from datetime import datetime

# # Припустимо, є timestamp
# timestamp = 1617183600

# # Конвертація timestamp назад у datetime
# dt_object = datetime.fromtimestamp(timestamp)
# print(dt_object)  # Виведе відповідний datetime


# from datetime import datetime

# now = datetime.now()

# # Форматування дати і часу
# formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
# print(formatted_date) 

# # Форматування лише дати
# formatted_date_only = now.strftime("%A, %d %B %Y")
# print(formatted_date_only)

# # Форматування лише часу
# formatted_time_only = now.strftime("%I:%M %p")
# print(formatted_time_only)  

# # Форматування лише дати
# formatted_date_only = now.strftime("%d.%m.%Y")
# print(formatted_date_only)


# from datetime import datetime

# # Поточна дата та час
# now = datetime.now()

# # Конвертація у формат ISO 8601
# iso_format = now.isoformat()
# print(iso_format)


# from datetime import datetime

# iso_date_string = "2023-03-14T12:39:29.992996"

# # Конвертація з ISO формату
# date_from_iso = datetime.fromisoformat(iso_date_string)
# print(date_from_iso)


# from datetime import datetime

# # Створення об'єкта datetime
# now = datetime.now()

# # Використання isoweekday() для отримання дня тижня
# day_of_week = now.isoweekday()

# print(f"Сьогодні: {day_of_week}")  # Поверне число від 1 до 7, що відповідає дню тижня


# from datetime import datetime

# # Створення об'єкта datetime
# now = datetime.now()

# # Отримання ISO календаря
# iso_calendar = now.isocalendar()

# print(f"ISO рік: {iso_calendar[0]}, ISO тиждень: {iso_calendar[1]}, ISO день тижня: {iso_calendar[2]}")


# from datetime import datetime, timezone

# local_now = datetime.now()
# utc_now = datetime.now(timezone.utc)

# print(local_now)
# print(utc_now)  # Виведе поточний час в UTC


# from datetime import datetime, timezone, timedelta

# utc_time = datetime.now(timezone.utc)

# # Створення часової зони для Східного часового поясу (UTC-5)
# eastern_time = utc_time.astimezone(timezone(timedelta(hours=-5)))
# # Перетворює час UTC в час Східного часового поясу
# print(eastern_time)


# from datetime import datetime, timezone, timedelta

# # Припустимо, місцевий час належить до часової зони UTC+2
# local_timezone = timezone(timedelta(hours=2))
# local_time = datetime(year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=local_timezone)

# # Конвертація локального часу в UTC
# utc_time = local_time.astimezone(timezone.utc)
# print(utc_time)  # Виведе час в UTC


# from datetime import datetime, timezone, timedelta

# # Час у конкретній часовій зоні
# timezone_offset = timezone(timedelta(hours=2))  # Наприклад, UTC+2
# timezone_datetime = datetime(year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=timezone_offset)

# # Конвертація у формат ISO 8601
# iso_format_with_timezone = timezone_datetime.isoformat()
# print(iso_format_with_timezone)


# import time

# current_time = time.time()
# print(f"Поточний час: {current_time}")


# import time

# print("Початок паузи")
# time.sleep(5)
# print("Кінець паузи")


# from datetime import datetime, timedelta

# def string_to_date(date_string):
#     return datetime.strptime(date_string, "%Y.%m.%d").date()

# def date_to_string(date):
#     return date.strftime("%Y.%m.%d")

# def is_weekend(date):
#     return date.weekday() in (5, 6)

# def next_working_day(date):
#     while is_weekend(date):
#         date += timedelta(days=1)
#     return date

# def get_upcoming_birthdays(users):
#     today = datetime.today().date()
#     next_week = today + timedelta(days=7)
    
#     upcoming_birthdays = []
    
#     for user in users:
#         birthday = string_to_date(user["birthday"])
#         birthday_this_year = birthday.replace(year=today.year)

#         if today <= birthday_this_year <= next_week:
#             birthday_this_year = next_working_day(birthday_this_year)
#             upcoming_birthdays.append({
#                 "name": user["name"],
#                 "birthday": date_to_string(birthday_this_year)
#             })
    
#     return upcoming_birthdays

# users = [
#     {"name": "Bill Gates", "birthday": "1955.3.25"},
#     {"name": "Steve Jobs", "birthday": "1955.3.21"},
#     {"name": "Jinny Lee", "birthday": "1956.3.22"},
#     {"name": "Sarah Lee", "birthday": "1957.3.23"},
#     {"name": "Jonny Lee", "birthday": "1958.3.22"},
#     {"name": "John Doe", "birthday": "1985.01.23"},
#     {"name": "Jane Smith", "birthday": "1990.01.27"}
# ]

# print(get_upcoming_birthdays(users))


# from datetime import datetime

# users = [
#     {"name": "Bill Gates", "birthday": "1955.3.25"},
#     {"name": "Steve Jobs", "birthday": "1955.3.21"},
#     {"name": "Jinny Lee", "birthday": "1956.3.22"},
#     {"name": "John Doe", "birthday": "1985.01.23"},
#     {"name": "Jane Smith", "birthday": "1990.01.27"}
# ]

# def string_to_date(date_string):
#     return datetime.strptime(date_string, "%Y.%m.%d").date()

# def prepare_user_list(user_data):
#     return [{"name": user["name"], "birthday": string_to_date(user["birthday"])} for user in user_data]

# prepared_users = prepare_user_list(users)
# print(prepared_users)


# from datetime import datetime, timedelta

# start_date = datetime.now()
# weekday = 4

# def string_to_date(date_string):
#     return datetime.strptime(date_string, "%Y.%m.%d").date()

# def find_next_weekday(start_date, weekday):
#     days_ahead = (weekday - start_date.weekday()) % 7
#     days_ahead = days_ahead if days_ahead else 7
#     return start_date + timedelta(days=days_ahead)

# print(find_next_weekday(start_date, weekday))


# from datetime import datetime, date, timedelta

# def string_to_date(date_string):
#     return datetime.strptime(date_string, "%Y.%m.%d").date()

# def date_to_string(date):
#     return date.strftime("%Y.%m.%d")

# def prepare_user_list(user_data):
#     prepared_list = []
#     for user in user_data:
#         prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
#     return prepared_list

# def get_upcoming_birthdays(users, days=7):
#     upcoming_birthdays = []
#     today = date.today()
#     end_date = today + timedelta(days=days)
#     for user in users:
#         birthday_this_year = user["birthday"].replace(year=today.year)
#         if today <= birthday_this_year <= end_date:
#             upcoming_birthdays.append({
#                 "name": user["name"],
#                 "congratulation_date": date_to_string(birthday_this_year)
#             })
#     return upcoming_birthdays

# users = [
#     {"name": "Sarah Lee", "birthday": "1957.03.30"},
#     {"name": "John Doe", "birthday": "1985.03.28"},
#     {"name": "Jane Smith", "birthday": "1990.03.27"},
#     {"name": "John Doe", "birthday": "1985.01.23"},
# ]

# print(get_upcoming_birthdays(prepare_user_list(users), 7))


# from datetime import datetime, timedelta


# def string_to_date(date_string):
#     return datetime.strptime(date_string, "%Y.%m.%d").date()


# def find_next_weekday(start_date, weekday):
#     days_ahead = weekday - start_date.weekday()
#     if days_ahead <= 0:
#         days_ahead += 7
#     return start_date + timedelta(days=days_ahead)


# def adjust_for_weekend(birthday):
#     if birthday.weekday() == 5:
#         return birthday + timedelta(days=2)
#     elif birthday.weekday() == 6:
#         return birthday + timedelta(days=1)
#     else:
#         return birthday 
#     return birthday


from datetime import datetime, date, timedelta


def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()


def date_to_string(date):
    return date.strftime("%Y.%m.%d")


def prepare_user_list(user_data):
    prepared_list = []
    for user in user_data:
        prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
    return prepared_list


def find_next_weekday(start_date, weekday):
    days_ahead = weekday - start_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)


def adjust_for_weekend(birthday):
    if birthday.weekday() >= 5:
        return find_next_weekday(birthday, 0)
    return birthday


def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []
    today = date.today()
    end_date = today + timedelta(days=days)
    for user in users:
        birthday_this_year = user["birthday"].replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        if today <= birthday_this_year <= end_date:
            adjusted_birthday = adjust_for_weekend(birthday_this_year)
            congratulation_date_str = date_to_string(adjusted_birthday)
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date_str})

    return upcoming_birthdays


users = [
    {"name": "Bill Gates", "birthday": "1955.3.25"},
    {"name": "Steve Jobs", "birthday": "1955.3.21"},
    {"name": "Jinny Lee", "birthday": "1956.3.22"},
    {"name": "Sarah Lee", "birthday": "1957.3.23"},
    {"name": "Jonny Lee", "birthday": "1958.3.22"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

print(get_upcoming_birthdays(prepare_user_list(users), 7))
