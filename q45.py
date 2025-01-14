# P.213

N = 9

if __name__ == '__main__':
    if N <= 3:
        print('0')
    else:
        factorial = 1
        for i in range(1, N + 1):
            factorial *= i
        print(factorial * (N - 3) // 6)
