# P.165

N = 12


def search(bw: int, fw: int, memo: dict) -> int:
    if memo.get((bw, fw)):
        return memo[(bw, fw)]

    if fw == 0:
        return 0

    count = 0
    for i in range(1, fw + 1):
        count += search(bw=fw - i, fw=bw + i - 1, memo=memo)

    memo[(bw, fw)] = count
    return count


if __name__ == '__main__':
    memo = {(0, 0): 1}
    if (N % 2 == 0):
        print(search(bw=0, fw=N - 2, memo=memo))
    else:
        print(0)
