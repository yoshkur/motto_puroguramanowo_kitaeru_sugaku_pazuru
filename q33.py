# P.161

M, N = 543210, 987654

if __name__ == '__main__':
    x = 2 * M - N
    if x > 0:
        print((3 * M - N) // 2 - x + 1)
    else:
        print((3 * M - N) // 2 + 1)
