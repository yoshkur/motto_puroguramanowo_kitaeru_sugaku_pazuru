# P.305

from copy import deepcopy
from itertools import product

N = 7


def queen(rows: list, n: int, left: int, down: int, right: int, queens: list):
    if n == N:
        queens.append(deepcopy(rows))
        return

    for i in range(N):
        pos = 1 << i
        if (pos & (left | down | right)) == 0:
            rows[n] = pos
            l, d, r = left | pos, down | pos, right | pos
            queen(rows=rows, n=n + 1, left=l << 1, down=d, right=r >> 1, queens=queens)


if __name__ == '__main__':
    queens = []
    queen(rows=[0] * N, n=0, left=0, down=0, right=0, queens=queens)
    white, black = [0] * N, [(1 << N) - 1] * N
    fw_log, bw_log = {tuple(white): 0}, {tuple(black): 0}
    fw, bw = [white], [black]

    depth = 1
    while True:
        fw_next = []
        for f, q in product(fw, queens):
            check = [0] * N
            for i in range(N):
                check[i] = f[i] ^ q[i]
            if tuple(check) not in fw_log.keys():
                fw_next.append(check)
                fw_log[tuple(check)] = depth

        fw = fw_next
        if len(fw) == 0 or len(set(map(tuple, fw)) & set(map(tuple, bw))) > 0:
            break

        depth += 1

        bw_next = []
        for b, q in product(bw, queens):
            check = [0] * N
            for i in range(N):
                check[i] = b[i] ^ q[i]
            if not bw_log.get(tuple(check)):
                bw_next.append(check)
                bw_log[tuple(check)] = depth

        bw = bw_next
        if len(bw) == 0 or len(set(map(tuple, fw)) & set(map(tuple, bw))) > 0:
            break

        depth += 1

    if len(set(map(tuple, fw)) & set(map(tuple, bw))) > 0:
        print(depth)
    else:
        print(0)
