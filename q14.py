# P.77

from itertools import combinations

N = 45678

if __name__ == '__main__':
    coins = [10000, 5000, 2000, 1000, 500, 100, 50, 10, 5, 1]
    result = N

    for i in range(10, 0, -1):
        for coin in combinations(iterable=coins, r=i):
            remain = N - sum(coin)
            if remain < 0:
                continue
            count = len(coin)
            for c in coin:
                r = remain // c
                count += r
                remain -= c * r
            result = min(count, result)
        if result < N:
            break

    print(result)
