# P.151

from itertools import permutations


N = 8


if __name__ == '__main__':
    unsort = 0
    sorted_ = list(range(1, N + 1))
    for tpl in permutations(sorted_, N):
        ary = list(tpl)
        for j in range(N):
            pos = ary[j] - 1
            ary[j], ary[pos] = ary[pos], ary[j]

        if ary != sorted_:
            unsort += 1

    print(unsort)
