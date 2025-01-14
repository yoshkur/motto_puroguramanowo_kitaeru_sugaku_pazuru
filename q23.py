# P.117

N = 100


def splits(n: int, memo: dict) -> int:
    if memo.get(n):
        return memo[n]

    result = 0
    if n < 6:
        result += 1

    for i in range(2, 6):
        if n - i * 2 > 1:
            result += splits(n=n - i * 2, memo=memo)
        if n - i * 2 == 0:
            result += 1
    memo[n] = result
    return result


if __name__ == '__main__':
    memo = {}
    count = 0
    for i in range(2, N):
        if N % i == 0:
            count += splits(n=i, memo=memo)

    print(count)
