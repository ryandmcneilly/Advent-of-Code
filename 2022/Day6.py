def solution(raw: str):
    l, r = 0, 3

    while len(set(raw[l:r+1])) != 4:
        l += 1
        r += 1

    print(r+1)


def solution2(raw: str):
    l, r = 0, 13

    while len(set(raw[l:r+1])) != 14:
        l += 1
        r += 1

    print(r+1)