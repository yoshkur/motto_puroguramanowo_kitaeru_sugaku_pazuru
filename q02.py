# P.29

N = 29

a, b = 1, 17

n = abs(a - b)

if __name__ == '__main__':
    print((1 << (n - 1)) + (1 << (N - n -1)) - 1)
    # print(2 ** (n - 1) + (2 ** (N - n - 1)) - 1)
