# P.99

RUNNER, HOOK = 50, 35


def search(runner: int, hook: int, memo: dict) -> int:
    if memo.get((runner, hook)):
        return memo[(runner, hook)]

    if hook <= 1:
        return 0
    if runner < hook:
        return 0

    count = 0
    count += search(runner=runner - 1, hook=hook - 1, memo=memo)
    count += search(runner=runner - 2, hook=hook - 1, memo=memo)
    memo[(runner, hook)] = count
    return count


if __name__ == '__main__':
    memo = {(2, 2): 1, (3, 2): 1}
    print(search(runner=RUNNER, hook=HOOK, memo=memo))
