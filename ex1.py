#Завантажуєм модуль
from datetime import datetime
#Створюєм функцію
def get_days_from_today (now_date, date):
    diff = now_date - date
    return diff.days
#Вписуєм параметри для дат
my_date ='2000-01-01'
date = datetime.strptime(my_date, '%Y-%m-%d')
print(date.month)
now_date = datetime.now()
#Задаєм параметри функціі
days = get_days_from_today (now_date, date)
#Виносимо результат
print(f'get_days_from_today,{my_date} {days}  days')