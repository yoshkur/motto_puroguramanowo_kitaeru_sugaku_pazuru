# P.169

N = 32


def check(bill: int, remain: int, memo: dict) -> int:
    if memo.get((bill, remain)):
        return memo[(bill, remain)]

    if remain == 0:
        return 1

    count = check(bill=bill + 3, remain=remain - 1, memo=memo)
    if bill >= 2:
        count += check(bill=bill - 2, remain=remain - 1, memo=memo)

    memo[(bill, remain)] = count
    return count


if __name__ == '__main__':
    memo = {}
    print(check(bill=0, remain=N, memo=memo))
