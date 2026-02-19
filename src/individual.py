#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    # Ввод номера месяца
    month = int(input("Введите номер месяца (1-12): "))

    # Проверка и вывод количества дней в месяце
    if month in (1, 3, 5, 7, 8, 10, 12):
        print("В этом месяце 31 день")
    elif month in (4, 6, 9, 11):
        print("В этом месяце 30 дней")
    elif month == 2:
        print("В этом месяце 28 дней")
    else:
        print("Ошибка: номер должен быть от 1 до 12", file=sys.stderr)
        sys.exit(1)
