# P.135

H, W, N = 20, 20, 10


def cut(h: int, w: int, n: int, memo: dict) -> int:
    if memo.get((h, w, n)):
        return memo[(h, w, n)]
    if n == 1:
        return 1

    count = 0
    for i in range(1, h):
        count += cut(h=i, w=w, n=n - 1, memo=memo)
    for i in range(1, w):
        count += cut(h=h, w=i, n=n - 1, memo=memo)
    memo[(h, w, n)] = count
    return count


if __name__ == '__main__':
    memo = {}
    print(cut(h=H, w=W, n=N, memo=memo))
