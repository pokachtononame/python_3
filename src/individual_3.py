#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    # Найти сумму целых положительных чисел > 20 и < 100, кратных 3
    total = 0
    for number in range(21, 100):
        if number % 3 == 0:
            total += number
    print(f"Сумма чисел больше 20 и меньше 100, кратных 3, равна: {total}")