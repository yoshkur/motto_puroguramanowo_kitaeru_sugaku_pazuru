# P.127

N = 39


def tree(n: int, memo: dict) -> int:
    if memo.get(n):
        return memo[n]

    count = 0
    for i in range(1, n + 1):
        count += tree(n=i - 1, memo=memo) * tree(n=n - i, memo=memo)

    memo[n] = count
    return count


if __name__ == '__main__':
    memo = {0: 1, 1: 1}

    if N % 2 == 0:
        print(0)
    else:
        print(tree(n=(N - 1) // 2, memo=memo))
