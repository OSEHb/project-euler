'''Задача 17'''
# Если записать числа от 1 до 5 английскими словами (one, two, three, four, five),
# используется всего 3 + 3 + 5 + 4 + 4 = 19 букв.
# Сколько букв понадобится для записи всех чисел от 1 до 1000 (one thousand) включительно?
# Примечание: Не считайте пробелы и дефисы. Например, число 342 (three hundred and forty-two) состоит из 23 букв,
# число 115 (one hundred and fifteen) - из 20 букв.
# Использование "and" при записи чисел соответствует правилам британского английского.

from num2words import num2words  # Переводит цифры в слово

result = 0

for i in range(1, 1001):  # Выводим цифру
    for x in num2words(i):  # Переводим в слово и берём первую букву(Х)
        if x.isalpha():  # Если х буква, то + 1
            result += 1

print(result)