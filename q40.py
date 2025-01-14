# P.193

from itertools import product

N = 12


def check(island: list) -> dict:
    pos = [0, N]
    q = [pos]
    log = {}
    log[tuple(pos)] = 0
    while len(q):
        left, right = q.pop(0)
        for dl, dr in product([-1, 1], repeat=2):
            l, r = left + dl, right + dr
            if l == r:
                return log[(left, right)] + 2
            if l >= 0 and r <= N and island[l] == island[r]:
                if l < r and tuple([l, r]) not in log.keys():
                    q.append([l, r])
                    log[(l, r)] = log[(left, right)] + 2
    return -1


def search(island: list, left: int, level: int):
    island[left] = level
    if left == N:
        return check(island=island)

    max_ = -1
    if level > 0:
        max_ = max(max_, search(island=island, left=left + 1, level=level - 1))
    if left + level < N:
        max_ = max(max_, search(island=island, left=left + 1, level=level + 1))

    return max_


if __name__ == '__main__':
    print(search(island=[-1] * (N + 1), left=0, level=0))
