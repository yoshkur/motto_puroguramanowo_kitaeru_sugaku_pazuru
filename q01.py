# P.25

N = 100

if __name__ == '__main__':
    count = 0
    for rock in range(N + 1):
        for scissors in range(N - rock + 1):
            paper = N - rock - scissors
            all_ = [rock, scissors, paper]
            if all_.count(max(all_)) == 1:
                count += 1

    print(count)
