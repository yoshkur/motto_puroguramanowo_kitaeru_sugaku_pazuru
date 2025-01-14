# P.261

M, N = 10, 6


def check(m: int, n: int) -> int:
    if n == 1:
        return 3

    count = (3 + (m - 1) * (m - 2) // 2) * check(m=m, n=n - 1)
    for i in range(2, m):
        count += 3 * check(m=i, n=n - 1)

    return count


if __name__ == '__main__':
    print(check(m=M, n=N))
