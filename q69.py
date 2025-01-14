# P.331

N = 25


def split(n: int, pre: int, memo: dict) -> list:
    key = tuple([n, pre])
    if memo.get(key):
        return memo[key]

    result = []
    for i in range(pre, (n - 1) // 2 + 1):
        result.append([i, n - i])
        for j in split(n=n - i, pre=i + 1, memo=memo):
            result.append([i] + j)
    memo[key] = result
    return result


def search(used: list, pos: int, memo: dict):
    if len(used) == pos:
        return 1

    count = search(used=used, pos=pos + 1, memo=memo)
    for i in split(n=used[pos], pre=1, memo=memo):
        if len(set(used) & set(i)) == 0:
            count += search(used=used + i, pos=pos + 1, memo=memo)

    return count


if __name__ == '__main__':
    memo = {}
    print(search(used=[N], pos=0, memo=memo))
