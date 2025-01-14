# P.313

M, N = 20, 100


def search(m: int, n: int, vote: list) -> int:
    if m == 0:
        if n == 0:
            return 1
        else:
            return 0

    count = 0
    for i in range(vote[m], n // m + 1):
        vote[m - 1] = i
        if vote[m - 1] % vote[M - 1] == 0:
            count += search(m=m - 1, n=n - i, vote=vote)

    return count


if __name__ == '__main__':
    print(search(m=M, n=N, vote=[0] * M + [1]))
