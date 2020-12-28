# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решите следующую задачу: напишите программу, которая будет генерировать матрицу из
# случайных целых чисел. Пользователь может указать число строк и столбцов, а также
# диапазон целых чисел. Произведите обработку ошибок ввода пользователя.

from random import randint

try:
    import random

    A = int(input('Введите кол-во срок: '))
    B = int(input('Введите кол-во столбцов: '))
    c = int(input('Введите 1 число: '))
    d = int(input('Введите 2 число: '))
    lst = [[randint(c, d) for i in range(A)] for i in range(B)]
    if c != d:
        for i in lst:
            print()
            for j in i:
                print(j, end=" ")
    else:
        raise ValueError()
except ValueError:
    print("Введите разные числа!")
else:
    print("\nКод выполнен без ошибок!")
finally:
    print("Выполняется всегда!")
