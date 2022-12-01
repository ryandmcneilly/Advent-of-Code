def solution(input: str):
    new = input.split("\n\n")

    for r in range(0, len(new)):
        new[r] = sum([int(i) for i in new[r].split("\n")])
    new.sort()

    print(new[-1]) # Q1
    print(new[-1] + new[-2] + new[-3])  # Q2
