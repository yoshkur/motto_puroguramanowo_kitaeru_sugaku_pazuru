# P.131

A, B, LIMIT = 10, 10, 24


def game(a: int, b: int, limit: int, memo: dict) -> int:
    if memo.get((a, b, limit)):
        return memo[(a, b, limit)]

    if a == 0 or b == 0:
        return 1

    if limit == 0:
        return 0

    count = 0
    count += game(a=a + 1, b=b - 1, limit=limit - 1, memo=memo)
    count += game(a=a, b=b, limit=limit - 1, memo=memo)
    count += game(a=a - 1, b=b + 1, limit=limit - 1, memo=memo)
    memo[(a, b, limit)] = count
    return count


if __name__ == '__main__':
    memo = {}
    print(game(a=A, b=B, limit=LIMIT, memo=memo))
