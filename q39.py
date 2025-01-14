# P.187

N = 11


def pair(n: int, memo: dict) -> int:
    if memo.get(n):
        return memo[n]

    if n == 1:
        return 0

    if n == 2:
        return 1

    result = (2 * (n - 1) + 1) * pair(n=n - 1, memo=memo) + pair(n=n - 2, memo=memo)
    memo[n] = result
    return result


if __name__ == '__main__':
    memo = {1: 0, 2: 1}
    print(pair(n=N, memo=memo))
