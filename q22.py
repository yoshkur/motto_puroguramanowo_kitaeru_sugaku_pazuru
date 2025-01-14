# P.111

COL = [8, 6, 8, 9, 3, 4, 1, 7, 6, 1]
ROW = [5, 1, 1, 9, 1, 6, 9, 0, 9, 6]

if __name__ == '__main__':
    board = []
    for i in ROW:
        temp_row = []
        for j in COL:
            temp_row.append(i + j)
        board.append(temp_row)

    for i in range(len(ROW)):
        for j in range(len(COL)):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                board[i][j] += board[i][j - 1]
            elif j == 0:
                board[i][j] += board[i - 1][j]
            else:
                board[i][j] += min(board[i][j - 1], board[i - 1][j])

    print(board[len(ROW) - 1][len(COL) - 1])
