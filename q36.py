# P.173

N = 12


def check(n: int) -> int:
    if n <= 1:
        return n

    return 7 * check(n=n - 2) + 3 * (7 ** (n - 1))


if __name__ == '__main__':
    print(check(n=N))
