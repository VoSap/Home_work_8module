from datetime import datetime, timedelta
from collections import defaultdict

users = [
    {'name': 'Ivan', 'birthday': datetime(1990, 5, 1)},
    {'name': 'Vova', 'birthday': datetime(1985, 4, 30)},
    {'name': 'Oksana', 'birthday': datetime(1995, 5, 2)},
    {'name': 'Volo', 'birthday': datetime(1985, 5, 5)},
    {'name': 'Vovik', 'birthday': datetime(1985, 5, 6)},
]


def get_birthdays_per_week(users):
    today = datetime.now().date()
    next_week = today + timedelta(days=7)
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    birthdays = defaultdict(list)

    for user in users:
        birthday = user['birthday'].replace(year=today.year).date()
        if birthday >= today and birthday <= next_week:
            weekday = weekdays[birthday.weekday()]
            if weekday in ['Saturday', 'Sunday']:
                weekday = 'Monday'
            birthdays[weekday].append(user['name'])

    for weekday in weekdays:
        if weekday in birthdays:
            print(f"{weekday}: {', '.join(birthdays[weekday])}")


get_birthdays_per_week(users)
