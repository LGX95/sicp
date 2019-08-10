#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ackermann function python version
"""


def ackermann(x, y):
    if y == 0:
        return 0
    elif x == 0:
        return y * 2
    elif y == 1:
        return 2
    else:
        return ackermann(x - 1, ackermann(x, y - 1))


if __name__ == '__main__':
    print(ackermann(1, 10))
    print(ackermann(2, 4))
    print(ackermann(3, 3))
