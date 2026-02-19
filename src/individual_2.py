#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    x = float(input("Введите x: "))
    y = float(input("Введите y: "))

    # Вычисление значения max^2(x^2 * y, x * y^2)
    if x ** 2 * y > x * y ** 2:
        maximum = (x ** 2 * y) ** 2
    else:
        maximum = (x * y ** 2) ** 2

    # Вычисление значения min^2(x - y, x + 2 * y)
    if x - y > x + 2 * y:
        minimum = (x + 2 * y) ** 2
    else:
        minimum = (x - y) ** 2

    u = maximum + minimum

    print(f'U = {u:.2f}')
