# P.147

CARDS, LIMIT = 32, 10


def check(remain: int, fw: int, turn: bool, memo: dict) -> int:
    if memo.get((remain, fw, turn)):
        return memo[(remain, fw, turn)]

    if remain == 0:
        return 1 if not turn and fw > CARDS // 2 else 0

    count = 0
    for i in range(1, LIMIT + 1):
        if turn:
            if remain >= i:
                count += check(remain=remain - i, fw=fw + i, turn=not turn, memo=memo)
        else:
            if remain >= i:
                count += check(remain=remain - i, fw=fw, turn=not turn, memo=memo)
    memo[(remain, fw, turn)] = count
    return count


if __name__ == '__main__':
    memo = {}
    print(check(remain=CARDS, fw=0, turn=True, memo=memo))
