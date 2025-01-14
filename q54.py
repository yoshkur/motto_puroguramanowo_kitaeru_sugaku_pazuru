# P.253

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,]

M, N = 50, 5


def search(remain: int, l: int, r: int, memo: dict) -> int:
    key = tuple([remain, l, r])
    if memo.get(key):
        return memo[key]
    if remain == 0:
        return 1 if l == r else 0

    count = 0
    use = PRIMES[remain - 1]
    count += search(remain=remain - 1, l=l + use, r=r, memo=memo)
    count += search(remain=remain - 1, l=l, r=r + use, memo=memo)
    count += search(remain=remain - 1, l=l, r=r, memo=memo)
    memo[key] = count
    return count


if __name__ == '__main__':
    memo = {}
    print(search(remain=len(PRIMES), l=N, r=0, memo=memo))
