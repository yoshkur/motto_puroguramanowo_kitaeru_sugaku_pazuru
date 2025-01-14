# P.37
from itertools import product

N = 30


def check(num: int) -> int:
    light = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    return light[num // 10] + light[num % 10]


if __name__ == '__main__':
    lights = [0] * 60
    for i in range(60):
        lights[i] = check(num=i)

    count = 0
    for h, m, s in product(range(24), range(60), range(60)):
        if lights[h] + lights[m] + lights[s] == N:
            count += 1

    print(count)
