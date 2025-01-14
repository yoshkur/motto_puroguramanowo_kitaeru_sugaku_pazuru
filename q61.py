# P.285

N = 20


def nCr(n: int, r: int, memo: dict) -> int:
    key = tuple([n, r])
    if memo.get(key):
        return memo[key]

    if r == 0 or r == n:
        return 1

    result = nCr(n=n - 1, r=r - 1, memo=memo) + nCr(n=n - 1, r=r, memo=memo)
    memo[key] = result
    return result


def tall(n: int, memo: dict, memo_tall: dict) -> int:
    if n <= 2:
        return 1
    if memo_tall.get(n):
        return memo_tall[n]

    result = 0
    for i in range(1, n + 1):
        result += tall(n=i - 1, memo=memo, memo_tall=memo_tall) * nCr(n=n - 1, r=i - 1, memo=memo) * tall(n=n - i, memo=memo, memo_tall=memo_tall)

    result_value = result // 2
    memo_tall[n] = result_value
    return result_value


if __name__ == '__main__':
    memo = {}
    memo_tall = {}

    if N == 1:
        print(1)
    else:
        print(2 * tall(n=N, memo=memo, memo_tall=memo_tall))
