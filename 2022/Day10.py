def solution(raw: str):
    raw = raw.split("\n")

    data = [1]
    for line in raw:
        data.append(data[-1])
        if line.startswith("addx"):
            data.append(int(line.split(" ")[1]) + data[-1])

    output = 0
    for spec in range(20, 260, 40):
        output += data[spec - 1] * spec
    # Q1 answer
    print(output)

    result = [[None] * 40 for _ in range(6)]
    for r in range(240):
        result[r // 40][r % 40] = "#" if abs(data[r] - r % 40) <= 1 else " "

    # Q2 answer
    for i in result:
        print("".join(i))


solution(given)
