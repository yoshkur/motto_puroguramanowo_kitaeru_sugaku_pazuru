# P.95

N = 16


def steps(n: int) -> int:
    count = 0
    while n > 0:
        count += 1
        none_ = ~n
        movable = (none_ << 1) + 1
        n = (n & (~movable)) | ((n >> 1) & none_)
    return count


if __name__ == '__main__':
    sum_ = 0
    for i in range(1, 1 << N):
        sum_ += steps(n=i)

    print(sum_)
