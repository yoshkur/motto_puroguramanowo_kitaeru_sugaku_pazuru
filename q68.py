# P.323

N = 5


def search(n: int, flag: bool, left: str, right: str, l: list, c: str, r: list) -> int:
    if n == 0:
        if len(set(left + right)) == N:
            return 1
        else:
            return 0

    count = 0

    for i in range(len(c)):
        for j in range(len(l[i])):
            if flag:
                count += search(n=n - 1, flag=not flag, left=left + l[i][j], right=c[i] + r[i][j] + right, l=l, c=c, r=r)
            else:
                count += search(n=n - 1, flag=not flag, left=left + c[i] + r[i][j], right=l[i][j] + right, l=l, c=c, r=r)

    return count


if __name__ == '__main__':
    l = ['DHLPTXdh', 'AEIMQUYaei', 'BFJNRVZbfj']
    c = 'QUY'
    r = ['QRSTUVYZ', 'PQRSTUVXYZ', 'PQRSTUVXYZ']

    print(search(n=N, flag=True, left='', right='', l=l, c=c, r=r))
