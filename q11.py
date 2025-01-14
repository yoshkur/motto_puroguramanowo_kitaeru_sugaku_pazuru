# P.63

N = 7


def vote(n: int) -> int:
    if n <= 2:
        return 1
    count = 1
    count += vote(n=n - 1)
    for i in range(2, n):
        count += vote(n=i) * vote(n=n - 1)
    return count


if __name__ == '__main__':
    print(vote(n=N))
