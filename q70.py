# P.335

from math import ceil

M, N = 10, 12


if __name__ == '__main__':
    sum_ = M + N - 1
    ave = sum_ // M

    kind = 0
    for i in range(1, M + 1):
        if sum_ == ave * i + (ave + 1) * (M - i):
            kind = ceil(N * (i / ave + (M - i) / (ave + 1)))
            break

    print(kind)
