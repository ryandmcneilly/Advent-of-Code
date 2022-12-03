def solution(input: str):
    new = input.split("\n")
    new = [i.split(" ") for i in new][1:-1]

    score = {"X": 1, "Y": 2, "Z": 3}
    draw = {"A": "X", "B": "Y", "C": "Z"}
    win = {"A": "Y", "B": "Z", "C": "X"}
    lose = {"A": "Z", "B": "X", "C": "Y"}

    result = 0
    counter = 0
    for round in new:
        # Q1
        result += score.get(round[1])
        if ord(round[0]) - ord(round[1]) == -23:
            result += 3
        elif ord(round[0]) - ord(round[1]) in [-24, -21]:
            result += 6

        # Q2
        if round[1] == "Y":
            counter += 3
            counter += score.get(draw.get(round[0]))
        elif round[1] == "Z":
            counter += 6
            counter += score.get(win.get(round[0]))
        else:
            counter += score.get(lose.get(round[0]))

    # Q1
    print(result)
    # Q2
    print(counter)
