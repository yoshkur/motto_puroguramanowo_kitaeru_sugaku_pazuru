# P.93

MEMBER, LIFT = 32, 6


def board(remain: int, memo: dict) -> int:
    if memo.get(remain):
        return memo[remain]

    count = 0
    for i in range(1, LIFT + 1):
        if remain - i >= 0:
            count += board(remain=remain - i, memo=memo)
    memo[remain] = count
    return count


if __name__ == '__main__':
    memo = {0: 1, 1: 1}
    print(board(remain=MEMBER, memo=memo))
