# P.301

from math import comb


N = 98303

if __name__ == '__main__':
    width = None
    for i in range(1, N // 2 + 1):
        if comb(N, i) % 2 == 0:
            width = i
            break

    print(width)

    # m = bin(N)[::-1].index("0")
    # print(2 ** m if m else "")
