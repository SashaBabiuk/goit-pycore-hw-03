from datetime import datetime

def get_days_from_today(date:str) -> int:
    try:
        return datetime.now().toordinal() - datetime.strptime(date,'%Y-%m-%d').toordinal()
    except ValueError as e:
        print("Sorry we cant process you date, enter valid date")
        return -1

print(get_days_from_today('2020-10-09'))
print(get_days_from_today('2025-12-31'))
print(get_days_from_today('1990-01-01'))
print(get_days_from_today('2020-13-01'))
print(get_days_from_today('invalid-date'))