# P.181

from math import floor

W, H = 4, 4


def search(n: int, seat: int, memo: dict) -> int:
    if memo.get((n, seat)):
        return memo[(n, seat)]

    if n < 0:
        return 1

    count = 0
    for i in range(W * H):
        if floor(i / W) != floor(n / W) and i % W != n % W:
            if (seat & (1 << i)) == 0:
                count += search(n=n - 1, seat=seat | (1 << i), memo=memo)
    memo[(n, seat)] = count
    return count


if __name__ == '__main__':
    memo = {}
    print(search(n=W * H - 1, seat=0, memo=memo))
