# P.45

W, N = 1000, 20


def cut(w: int, h: int, n: int) -> bool:
    if w == h:
        return n == 0
    if w > h:
        w, h = h, w

    q = h // w
    r = h % w

    if n - q < 0 or r == 0:
        return n - q == 0
    else:
        return cut(w=w, h=r, n=n - q)


if __name__ == '__main__':
    count = 0
    for i in range(1, W + 1):
        for j in range(i, W + 1):
            if cut(w=i, h=j, n=N):
                count += 1

    print(count)
