# P.297

from math import gcd, lcm

M, N = 60, 60

if __name__ == '__main__':
    if M == N:
        min_, max_ = M, 2 * M
    elif gcd(M, N) == 1:
        min_, max_ = M * N, M * N
    else:
        min_, max_ = lcm(M, N), 2 * lcm(M, N)

    print(min_)
    print(max_)
