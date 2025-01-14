# P.239

from math import sqrt

N = 1587600


def has_square(used: list) -> bool:
    value = 1

    for i in used:
        value *= i
        sqr = int(sqrt(value))
        if value == sqr ** 2:
            return True
    return False


def seq(remain: int, used: list) -> int:
    if remain <= 1:
        return 1

    count = 0
    for i in [2, 3, 5, 6, 7, 8]:
        if remain % i == 0:
            if not has_square(used=used):
                count += seq(remain=remain // i, used=[i] + used)
    return count


if __name__ == '__main__':
    print(seq(remain=N, used=[]))
