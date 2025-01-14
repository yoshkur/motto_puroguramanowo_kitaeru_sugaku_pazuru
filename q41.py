# P.197

from itertools import product

W, H = 10, 10


def search(tile: list, pos: int, memo: dict):
    if pos < len(tile) and tile[pos] == 1:
        return search(tile=tile, pos=pos + 1, memo=memo)

    if memo.get((tuple(tile), pos)):
        return memo[(tuple(tile), pos)]

    if pos == W * H:
        return 1

    count = 0
    tiles = [[1, 1], [2, 2], [4, 2], [4, 4]]
    for px, py in tiles:
        check = True
        for x, y in product(range(px), range(py)):
            if pos % W >= W - x or pos // W >= H - y:
                check = False
            elif pos + x + y * W < len(tile) and tile[pos + x + y * W] == 1:
                check = False

        if not check:
            continue

        for x, y in product(range(px), range(py)):
            if pos + x + y * W < len(tile):
                tile[pos + x + y * W] = 1
        count += search(tile=tile, pos=pos + 1, memo=memo)
        for x, y in product(range(px), range(py)):
            if pos + x + y * W < len(tile):
                tile[pos + x + y * W] = 0
    memo[(tuple(tile.copy()), pos)] = count
    return count


if __name__ == '__main__':
    memo = {}
    print(search(tile=[0] * (W * H), pos=0, memo=memo))
