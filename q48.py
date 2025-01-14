# P.227

M, N = 16, 4
SUM_ = M * (M + 1) // 2
GOAL = SUM_ // N


def search(n: int, used: list, sum_: int, card: int) -> int:
    if n == 1:
        return 1

    count = 0
    used[card] = True
    sum_ += card
    if sum_ == GOAL:
        max_not_used_card = M - used[::-1].index(False)
        count += search(n=n - 1, used=used, sum_=0, card=max_not_used_card)
    else:
        for i in range(min([card - 1, GOAL - sum_]), 0, -1):
            if not used[i]:
                count += search(n=n, used=used, sum_=sum_, card=i)

    used[card] = False
    return count


if __name__ == '__main__':
    if SUM_ % N == 0:
        print(search(n=N, used=[False] * (M + 1), sum_=0, card=M))
    else:
        print('0')
