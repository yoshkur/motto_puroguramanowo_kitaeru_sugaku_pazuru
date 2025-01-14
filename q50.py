# P.235

M, N = 50, 4


def search(n: int, prev: int, used: int) -> int:
    if n == 0:
        return 1

    count = 0
    for i in range(prev, M + 1):
        if (used & (used << i)) == 0:
            count += search(n=n - 1, prev=i + 1, used=used | (used << i))

    return count


if __name__ == '__main__':
    print(search(n=N, prev=1, used=1))
