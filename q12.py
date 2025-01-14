# P.67

N = 11

if __name__ == '__main__':
    q = 1
    PI = int('314159265358')
    pow = 10 ** N

    while True:
        if q * PI // pow != q * (PI + 1) // pow:
            if q * (PI + 1) % pow > 0:
                print(q)
                exit()
        q += 1
