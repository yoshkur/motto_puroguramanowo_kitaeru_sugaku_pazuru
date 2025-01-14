# P.245

N = 16


if __name__ == '__main__':
    max_ = 0
    for i in range(1, N + 1):
        max_ = max(max_, i ** (N - i))

    print(max_)
