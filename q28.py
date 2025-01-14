# P.139

HOLE, PAR = 18, 72


def golf(hole: int, par: int, memo: dict) -> int:
    if memo.get((hole, par)):
        return memo[(hole, par)]
    # 解答通りだと数分経っても終わらないので終了条件を追加。
    if hole * 5 < par:
        return 0
    if hole <= 0 or par <= 0:
        return 0
    if hole == 1 and par <= 5:
        return 1

    count = 0
    for i in range(1, 6):
        count += golf(hole=hole - 1, par=par - i, memo=memo)
    memo[(hole, par)] = count
    return count


if __name__ == '__main__':
    memo = {}
    print(golf(hole=HOLE, par=PAR, memo=memo))
