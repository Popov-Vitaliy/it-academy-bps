"""Оглянемся назад. Числа"""
"""Даны два натуральных числа. Вычислите их наибольший общий делитель
при помощи алгоритма Евклида (мы не знаем функции и рекурсию)"""

a = int(input('Введите число А: '))
b = int(input('Введите число B: '))
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
print(a)
