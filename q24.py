# P.121

N = 12


def search(duo: int, trio: int, memo: dict) -> int:
    if memo.get((duo, trio)):
        return memo[(duo, trio)]

    if duo > N or trio > N:
        return 0

    count = 0
    if duo == trio:
        count += 2 * search(duo=duo + 1, trio=trio, memo=memo)
        count += search(duo=duo + 1, trio=trio + 1, memo=memo)
        count += search(duo=duo + 2, trio=trio, memo=memo)
    elif duo < trio:
        count += 2 * search(duo=duo + 1, trio=trio, memo=memo)
        count += search(duo=duo + 2, trio=trio, memo=memo)
    else:
        count += 4 * search(duo=duo, trio=trio + 1, memo=memo)
        count += search(duo=duo, trio=trio + 2, memo=memo)

    memo[(duo, trio)] = count
    return count


if __name__ == '__main__':
    memo = {(N, N): 1}
    print(search(duo=0, trio=0, memo=memo))
