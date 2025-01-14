# P.49

N = 15


def nPr(n: int, r: int) -> int:
    result = 1
    for i in range(r):
        result *= n - i
    return result


if __name__ == '__main__':
    count = 0
    for i in range(1, N):
        count += i * (N - i) * nPr(n=N, r=i - 1)
    print(count)
