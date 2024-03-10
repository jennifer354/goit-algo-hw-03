#Завантажуєм модуль
from datetime import datetime
#Створюєм функцію
def get_days_from_today (now_date, end_date):
    diff = now_date - end_date
    return diff.days
#Вписуєм параметри для дат
end_date = datetime(year=2023, month=12, day=18)
now_date = datetime.now()
#Задаєм параметри функціі
days = get_days_from_today (now_date, end_date)
#Виносимо результат
print(f'get_days_from_today,{end_date} {days}  days')