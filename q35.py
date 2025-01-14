# P.169
# 数分経っても終わらない

N = 32


def check(m: int, n: int, remain: int, memo: dict) -> int:
    if memo.get((m, n, remain)):
        return memo[(m, n, remain)]

    if m == 0 and n == 0:
        return 1

    count = 0
    if m > 0:
        count += check(m=m - 1, n=n, remain=remain + 3, memo=memo)
    if n > 0:
        if remain >= 2:
            count += check(m=m, n=n - 1, remain=remain - 2, memo=memo)

    memo[(m, n, remain)] = count
    return count


if __name__ == '__main__':
    memo = {}
    count = 0
    for i in range(N + 1):
        count += check(m=i, n=N - 1, remain=0, memo=memo)

    print(count)
