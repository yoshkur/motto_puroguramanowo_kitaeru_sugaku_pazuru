# P.291

from copy import deepcopy

W, H = 10, 7


def check(temp: list) -> int:
    connect = [0] * W * H
    remain, single = 0, 0

    for i in range(W * H):
        if temp[i] == 0:
            connect[i] += 1 if i % W and temp[i - 1] == 0 else 0
            connect[i] += 1 if i % W != W - 1 and temp[i + 1] == 0 else 0
            connect[i] += 1 if i // W and temp[i - W] == 0 else 0
            connect[i] += 1 if i // W != H - 1 and temp[i + W] == 0 else 0
            remain += 1
            single += 1 if connect[i] == 1 else 0

    if single > 0:
        for i in range(W * H):
            if connect[i] == 1 and temp[i] == 0:
                temp[i] = 1
                if i % W and temp[i - 1] == 0:
                    temp[i - 1] = 1
                elif i % W != W - 1 and temp[i + 1] == 0:
                    temp[i + 1] = 1
                elif i // W and temp[i - W] == 0:
                    temp[i - W] = 1
                elif i // W != H - 1 and temp[i + W] == 0:
                    temp[i + W] = 1
                else:
                    return 1
        return check(temp=temp)
    else:
        return remain


def search(pos: int, depth: int, pins: list, broken: int) -> None:
    if depth == 0:
        if check(deepcopy(pins)) == 0:
            print(broken)
            exit()
        return

    if pos == W * H:
        return

    if pins[pos] == 0:
        if pos % W < W - 1 and pins[pos + 1] == 0:
            pins[pos], pins[pos + 1] = 1, 1
            search(pos=pos, depth=depth - 1, pins=pins, broken=broken)
            pins[pos], pins[pos + 1] = 0, 0

        if pos // W < H - 1 and pins[pos + W] == 0:
            pins[pos], pins[pos + W] = 1, 1
            search(pos=pos, depth=depth - 1, pins=pins, broken=broken)
            pins[pos], pins[pos + W] = 0, 0

    search(pos=pos + 1, depth=depth, pins=pins, broken=broken)


if __name__ == '__main__':
    pins = [0] * W * H
    for i in range(W * H // 2):
        broken = i
        search(pos=0, depth=broken, pins=pins, broken=broken)
