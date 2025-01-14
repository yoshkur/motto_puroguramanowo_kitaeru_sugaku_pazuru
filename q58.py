# P.269

N = 15


def tree_count(n: int, memo: list) -> list:
    if len(memo) > n:
        return memo[n]

    all_, pair = 0, 0
    for i in range(1, n):
        la, lp = tree_count(n=i, memo=memo)
        ra, rp = tree_count(n=n - i, memo=memo)
        all_ += la * ra * 2
        pair += la * (2 * rp + ra // 2) + ra * (2 * lp + la // 2)

    memo.insert(n, [all_, pair])
    return [all_, pair]


if __name__ == '__main__':
    memo = [[0, 0], [1, 0]]
    all_, pair = tree_count(n=N, memo=memo)
    print(pair)
