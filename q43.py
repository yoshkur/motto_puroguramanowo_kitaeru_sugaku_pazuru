# P.205

from itertools import permutations

N = 7


if __name__ == '__main__':
    count = 0
    for seat in permutations(range(1, N + 1)):
        flag = True
        for i in range(len(seat)):
            if seat[i] - 1 == i or seat[i] - 1 == (i + 1) % N:
                flag = False
                break
        if flag:
            count += 1

    baisu = 1
    for i in range(1, N):
        baisu *= i
    print(count * baisu)
