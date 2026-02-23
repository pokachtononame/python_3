#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

EPS = 1e-10

if __name__ == '__main__':
    x = float(input("Value of x: "))
    # Начальное значение при n=1
    # A1 = ((-1)^1 * x^2) / (2*1 * (2*1)!) = -x^2 / 4
    n = 1
    a = -(x ** 2) / 4
    total_sum = a
    while math.fabs(a) > EPS:
        # an+1 = an * (-x^2 * n) / (2 * (n+1)^2 * (2n + 1))
        multiplier = -(x ** 2 * n) / (2 * (n + 1) ** 2 * (2 * n + 1))
        a *= multiplier
        total_sum += a
        n += 1

    print("Result: ", total_sum)
