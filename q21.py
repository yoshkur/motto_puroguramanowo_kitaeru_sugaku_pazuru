# P.107

PAGES, DAYS = 180, 14


def search(pages: int, prev: int, days: int, memo: dict) -> int:
    key = tuple([pages, prev, days])
    if memo.get(key):
        return memo[key]

    if pages == 0:
        return 1

    if pages < 0 or days == 0:
        return 0

    count = 0

    for i in range(1, prev):
        count += search(pages=pages - i, prev=i, days=days - 1, memo=memo)
    memo[key] = count
    return count


if __name__ == '__main__':
    memo = {}
    print(search(pages=PAGES, prev=PAGES + 1, days=DAYS, memo=memo))
