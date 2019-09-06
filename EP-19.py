'''Задача 19'''
# Дана следующая информация (однако, вы можете проверить ее самостоятельно):
# 1 января 1900 года - понедельник.
# В апреле, июне, сентябре и ноябре 30 дней.
# В феврале 28 дней, в високосный год - 29.
# В остальных месяцах по 31 дню.
# Високосный год - любой год, делящийся нацело на 4, однако последний год века (ХХ00) является високосным
# в том и только том случае, если делится на 400.
# Сколько воскресений выпадает на первое число месяца в двадцатом веке (с 1 января 1901 года до 31 декабря 2000 года)?

year = 1899
leap_year = -1
result = 0
sunday = 0
_31_day = [1, 3, 5, 7, 8, 10, 12]
_30_day = [4, 6, 9, 11]
_28_day = [2]
_29_day = [2]

while True:
    year += 1
    leap_year += 1
    if year == 1901:
        result = 0
    if year == 2001:
        break

    for month in range(1, 13):
        if month in _31_day:
            for day in range(1, 32):
                sunday += 1
                if sunday == 7 and day == 1:
                    result += 1
                    sunday = 0
                if sunday == 7:
                    sunday = 0
            continue
        if month in _30_day:
            for day in range(1, 31):
                sunday += 1
                if sunday == 7 and day == 1:
                    result += 1
                    sunday = 0
                if sunday == 7:
                    sunday = 0
            continue
        if leap_year < 4 and month in _28_day:
            for day in range(1, 29):
                sunday += 1
                if sunday == 7 and day == 1:
                    result += 1
                    sunday = 0
                if sunday == 7:
                    sunday = 0
            continue
        if leap_year == 4 and month in _29_day:
            leap_year = 0
            for day in range(1, 30):
                sunday += 1
                if sunday == 7 and day == 1:
                    result += 1
                    sunday = 0
                if sunday == 7:
                    sunday = 0

print(result)