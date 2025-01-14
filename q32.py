# P.157

from itertools import product


N = 14


if __name__ == '__main__':
    count = 0
    for i in product([0, 1], repeat=N):
        a = i.count(1)
        b = N - a
        if a > 1 and b > 1:
            count += (a - 1) * (b - 1)

    print(count)
