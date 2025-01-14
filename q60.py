# P.279

def check(board: list, user: int) -> bool:
    for i in range(3):
        if (user == board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2]) or (user == board[i] == board[i + 3] == board[i + 6]):
            return True

    if (user == board[0] == board[4] == board[8]) or (user == board[2] == board[4] == board[6]):
        return True

    return False


def search(board: list, user: int, memo: dict, uniq: dict) -> int:
    key = tuple([tuple(board), user])
    if memo.get(key):
        return memo[key]

    if check(board=board, user=-user):
        uniq[tuple(board)] = True
        return 1

    count = 0
    for i in range(9):
        if board[i] == 0:
            board[i] = user
            count += search(board=board, user=-user, memo=memo, uniq=uniq)
            board[i] = 0
    memo[key] = count
    return count


if __name__ == '__main__':
    memo = {}
    uniq = {}
    print(search(board=[0] * 9, user=1, memo=memo, uniq=uniq))
    print(len(uniq))
