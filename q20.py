# P.103

N, START, GOAL = 15, 3, 10


def search(used: list, pos: int, memo: dict) -> int:
    key = tuple([tuple(used), pos])
    if memo.get(key):
        return memo[key]

    if pos == GOAL:
        return 1

    count = 0
    used[pos - 1] = True
    if pos < GOAL:
        for i in range(GOAL, N + 1):
            if not used[i - 1]:
                count += search(used=used, pos=i, memo=memo)
    else:
        for i in range(1, GOAL + 1):
            if not used[i - 1]:
                count += search(used=used, pos=i, memo=memo)
    used[pos - 1] = False
    memo[key] = count
    return count


if __name__ == '__main__':
    memo = {}
    print(search(used=[False] * N, pos=START, memo=memo))
