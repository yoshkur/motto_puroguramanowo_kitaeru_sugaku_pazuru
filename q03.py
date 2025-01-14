# P.33

N = 12


def conv(n: int, i: str, v: str, x: str) -> str:
    result = ''
    if n == 9:
        result += i + x
    elif n == 4:
        result += i + v
    else:
        result += v * (n // 5)
        n = n % 5
        result += i * n
    return result


def roman(n: int) -> str:
    m = n // 1000
    n %= 1000
    c = n // 100
    n %= 100
    x = n // 10
    n %= 10
    result = 'M' * m
    result += conv(n=c, i='C', v='D', x='M')
    result += conv(n=x, i='X', v='L', x='C')
    result += conv(n=n, i='I', v='V', x='X')
    return result


if __name__ == '__main__':
    count = [0] * 3999
    for n in range(1, 4000):
        count[len(roman(n))] += 1

    print(count[N])
