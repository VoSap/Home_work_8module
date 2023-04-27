from datetime import datetime, timedelta
from collections import defaultdict

users = [
    {'name': 'Ivan', 'birthday': datetime(1990, 4, 28)},
    {'name': 'Vova', 'birthday': datetime(1985, 4, 27)},
    {'name': 'Oksana', 'birthday': datetime(1995, 5, 2)}
]


def get_birthdays_per_week(users):
    today = datetime.now().date()
    for user in users:
        user['birthday'] = user['birthday'].replace(year=today.year)
    next_week = today + timedelta(days=7)
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    birthdays = defaultdict(list)

    for user in users:
        birthday = user['birthday'].date()
        if birthday >= today and birthday <= next_week:
            weekday = weekdays[birthday.weekday()]
            if weekday in ['Saturday', 'Sunday']:
                weekday = 'Monday'
            birthdays[weekday].append(user['name'])

    for weekday in weekdays:
        if weekday in birthdays:
            print(f"{weekday}: {', '.join(birthdays[weekday])}")


get_birthdays_per_week(users)