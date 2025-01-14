# P.275

N, A, B = 11, 25, 24


def search(a: int, b: int, memo: dict) -> int:
    key = tuple([a, b])
    if memo.get(key):
        return memo[key]

    if a == A and b == B:
        return 1
    if (a >= N or b >= N) and (abs(a - b) > 1):
        return 0
    if a > A or b > B:
        return 0

    result = search(a=a + 1, b=b, memo=memo) + search(a=a, b=b + 1, memo=memo)
    memo[key] = result
    return result


if __name__ == '__main__':
    memo = {}
    print(search(a=0, b=0, memo=memo))
