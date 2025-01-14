# P.55

N = 8

if __name__ == '__main__':
    keta = 1
    while True:
        if keta * ((N - 1) ** keta) < N ** (keta - 1):
            break
        keta += 1

    count = 0
    for i in range(N, N ** keta + 1):
        value = oct(i)[2:]
        len_ = len(value)
        sum_ = 0
        for d in range(len_):
            sum_ += int(value[d]) ** len_

        if i == sum_:
            print(value)
            count += 1
            if count == N:
                break
