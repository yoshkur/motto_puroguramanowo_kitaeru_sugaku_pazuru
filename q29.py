# P.143

M, N, W = 20, 40, 10


def cut(m: int, n: int, min_: int, max_: int, memo: dict) -> int:
    if memo.get((m, n, min_, max_)):
        return memo[(m, n, min_, max_)]

    if max_ - min_ > W:
        return 0

    if m == 0:
        return 1 if n == 0 else 0

    count = 0
    for w in range(n + 1):
        count += cut(m=m - 1, n=n - w, min_=min(min_, w), max_=max(max_, w), memo=memo)
    memo[(m, n, min_, max_)] = count
    return count


if __name__ == '__main__':
    memo = {}
    print(cut(m=M, n=N, min_=N, max_=0, memo=memo))
