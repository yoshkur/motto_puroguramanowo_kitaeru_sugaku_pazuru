# P.87

from math import gcd

N = 1234567

if __name__ == '__main__':
    count = 0
    for i in range(1, N // 2 + 1):
        if gcd(i, N - i) == 1:
            count += 1

    print(count)
