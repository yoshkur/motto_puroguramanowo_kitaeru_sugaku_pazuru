# P.265

STATION, EXPRESS, LIMITED = 32, 12, 4


def search(s: int, e: int, l: int, memo: dict) -> int:
    key = tuple([s, e, l])
    if memo.get(key):
        return memo[key]

    if s == 0 and e == 0 and l == 0:
        return 1

    if s == 0 and (e > 0 or l > 0):
        return 0

    if e == 0 or l == 0:
        return 0

    count = 0
    count += search(s=s - 1, e=e - 1, l=l - 1, memo=memo)
    count += search(s=s - 1, e=e - 1, l=l, memo=memo)
    count += search(s=s - 1, e=e, l=l, memo=memo)
    memo[key] = count
    return count


if __name__ == '__main__':
    memo = {}
    print(search(s=STATION - 1, e=EXPRESS - 1, l=LIMITED - 1, memo=memo))
