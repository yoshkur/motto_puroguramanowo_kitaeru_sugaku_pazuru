# P.231

from fractions import Fraction

EXP = 10


def group_count(n: int, memo: dict) -> int:
    if memo.get(n):
        return memo[n]

    calc = Fraction(1, n) + group_count(n=n - 1, memo=memo)
    memo[n] = calc
    return calc


if __name__ == '__main__':
    memo = {1: 1}
    m = 1
    while group_count(n=m, memo=memo) <= EXP:
        m += 1
    print(m)
