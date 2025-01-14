# P.317

from itertools import combinations


W, H, N = 4, 7, 4

MASK = (1 << (W * H)) - 1


def enable(maze: int, move: list) -> bool:
    man = 1 << (W * H - 1) & (MASK - maze)
    while True:
        next_man = man
        for m in move:
            next_man |= m(man)
        next_man &= MASK - maze

        if next_man & 1 == 1:
            return True

        if man == next_man:
            break

        man = next_man
    return False


def search(maze: int, p1: int, d1: int, depth: int, move: list):
    if p1 == 1:
        return depth

    for i in range(len(move)):
        d = (d1 - 1 + i + len(move)) % len(move)
        if move[d](p1) & MASK - maze > 0:
            return search(maze=maze, p1=move[d](p1), d1=d, depth=depth + 1, move=move)
    return 0


if __name__ == '__main__':
    left, right = 0, 0
    for i in range(H):
        left = left << W | (1 << (W - 1)) - 1
        right = right << W | (1 << W) - 2

    move = [
        lambda m: (m >> 1) & left,  # 右
        lambda m: (m << W) & MASK,   # 上
        lambda m: (m << 1) & right,   # 左
        lambda m: m >> W              # 下
    ]

    max_ = 0
    for pos in combinations(range(W * H), N):
        maze = sum(1 << i for i in pos)
        if enable(maze=maze, move=move):
            man_a = 1 << (W * H - 1)
            max_ = max(search(maze=maze, p1=man_a, d1=3, depth=1, move=move), max_)

    print(max_)
