# P.71

from itertools import permutations, product

M, N = 9, 5

if __name__ == '__main__':
    seq = []
    for a in permutations(iterable=range(2, M + 1), r=M - 1):
        seq.append([1] + list(a))

    log = []
    log.append(seq)

    for i in range(N):
        seq = []
        for a, j in product(log[i], range(1, M)):
            if a[j] == j + 1:
                seq.append(a[:j + 1][::-1] + a[j + 1:])
        log.append(seq)

    print(len(log[N]))
