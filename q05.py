# P.41

N = 45


def count(n: int) -> int:
    coin = [10000, 5000, 2000, 1000, 500, 100, 50, 10, 5, 1]
    result = 0
    for c in coin:
        count_ = n // c
        n = n % c
        result += count_
    return result


if __name__ == '__main__':
    row = [0] * (N + 1)
    row[0] = 1

    for i in range(N):
        for j in range(i + 1, 0, -1):
            row[j] += row[j - 1]

    # print(sum(map(count, row)))
    sum_ = 0
    for i in row:
        sum_ += count(i)
    print(sum_)
