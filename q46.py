# P.217

W, H, N = 5, 4, 22
DIRECTIONS = {1: 0b1, W: 0b100, -1: 0b10, -W: 0b1000}


def search(pos: int, dir_: int, used: list, n: int) -> int:
    if n < 0:
        return 0

    if pos + dir_ == W * H - 1:
        return 1 if n == 0 else 0

    used[pos] |= DIRECTIONS[dir_]
    pos += dir_
    used[pos] |= DIRECTIONS[-dir_]

    count = 0
    for d, bit in DIRECTIONS.items():
        m = n - (0 if dir_ == d else 1)
        if (used[pos] & bit) == 0:
            count += search(pos=pos, dir_=d, used=used, n=m)

    used[pos] ^= DIRECTIONS[-dir_]
    pos -= dir_
    used[pos] ^= DIRECTIONS[dir_]
    return count


if __name__ == '__main__':
    used = [0] * W * H
    for w in range(W):
        used[w] |= DIRECTIONS[-W]
        used[w + (H - 1) * W] |= DIRECTIONS[W]
    for h in range(H):
        used[h * W] |= DIRECTIONS[-1]
        used[(h + 1) * W - 1] |= DIRECTIONS[1]

    count = 0
    count += search(pos=0, dir_=1, used=used, n=N)
    count += search(pos=0, dir_=W, used=used, n=N)
    print(count)
