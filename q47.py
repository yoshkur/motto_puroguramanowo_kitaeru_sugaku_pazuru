# P.221

from itertools import product

M, N = 6, 6


def compress(str_: str) -> int:
    len_ = 2
    pre = str_[0]
    for c in str_:
        if pre != c:
            pre = c
            len_ += 2

    return len_


if __name__ == '__main__':
    count = 0
    for str_ in product(range(1, M + 1), repeat=N):
        count += 1 if len(str_) > compress(str_=str_) else 0

    print(count)
