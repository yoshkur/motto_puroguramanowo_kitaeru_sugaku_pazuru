# P.203

W, H = 99, 101

if __name__ == '__main__':
    inside = (W - 1) * (H - 1) * 2
    outside = (W + H) * 2
    if W != 1 and H != 1 and (W % 2 == 0 or H % 2 == 0):
        print(inside + outside - 2)
    else:
        print(inside + outside)
