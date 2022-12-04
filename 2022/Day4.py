def solution(input: str):
    input = input.split("\n")
    input = [i.split(",") for i in input]

    for r in range(len(input)):
        for j in [0, 1]:
            input[r][j] = list(range(int(input[r][j].split("-")[0]),
                                     int(input[r][j].split("-")[1]) + 1))

    # Q1
    total = 0
    for pair in input:
        result0 = all(i in pair[0] for i in pair[1])
        result1 = all(i in pair[1] for i in pair[0])
        if result0 or result1:
            total += 1
    print(total)

    # Q2
    total = 0
    for pair in input:
        result0 = any(i in pair[0] for i in pair[1])
        result1 = any(i in pair[1] for i in pair[0])
        if result0 or result1:
            total += 1
    print(total)
