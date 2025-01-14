# P.257

from itertools import product

W, H = 6, 3


if __name__ == '__main__':
    mask = []
    for h, w in product(range(H), range(W)):
        pos = 1 << w + h * W
        if w > 0:
            pos |= 1 << w - 1 + h * W
        if w < W - 1:
            pos |= 1 << w + 1 + h * W
        if h > 0:
            pos |= 1 << w + (h - 1) * W
        if h < H - 1:
            pos |= 1 << w + (h + 1) * W
        mask.append(pos)

    checked = {0: 0, (1 << (W * H)) - 1: 0}
    queue = [0, (1 << (W * H)) - 1]
    n = 0
    while len(queue):
        temp = []
        for i, j in product(queue, mask):
            key = i ^ j
            if key not in checked or not checked[key]:
                temp.append(key)
                checked[key] = n
        queue = temp
        n += 1

    print(n - 1)
