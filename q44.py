# P.209

N = 12345


def trit(number: int) -> str:
    result = ''
    while number > 0:
        value = number % 3
        result = f'{value}{result}'
        number //= 3
    return result


if __name__ == '__main__':
    count = 0
    for i in range(N + 1):
        if trit(i).find('2') == -1:
            count += 1
    print(count)
