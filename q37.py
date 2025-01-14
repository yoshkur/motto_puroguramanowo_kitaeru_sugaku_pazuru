# P.177

M, N = 10, 50


def search(m: int, n: int, memo: dict) -> int:
    if memo.get((m, n)):
        return memo[(m, n)]

    if n < 0:
        return 0

    if m == 0:
        return 1 if n == 0 else 0

    count = 0
    for i in range(1, 10):
        count += search(m=m - 1, n=n - i, memo=memo)

    memo[(m, n)] = count
    return count


if __name__ == '__main__':
    memo = {}
    print(search(m=M, n=N, memo=memo))
