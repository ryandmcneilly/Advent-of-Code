def solution(raw: str):
    COLUMNS = 9
    raw = raw.split("\n\n")
    table = raw[0]
    instructions = raw[1].split("\n")

    table = table.split("\n")[:-1]

    table = [x.replace("    ", "_") for x in table]

    for char in "[] ":
        table = [x.replace(char, "") for x in table]

    new_table = [None] * COLUMNS

    for r in range(COLUMNS):
        for x in table:
            if x[r] != "_":
                new_table[r] = new_table[r] + x[r] if new_table[r] else x[r]
    # Here we have column by column parsing
    table = new_table

    instructions = ["_".join("_".join("".join(x.split(' '))[4:].split(
        "from")).split("to")).split("_") for x in instructions]

    # Turn string inputs into integers
    for r in range(len(instructions)):
        instructions[r] = [int(x) for x in instructions[r]]

    # Q1
    # for instruction in instructions:
    #     for i in range(instruction[0]):
    #         table[instruction[2] - 1] = table[instruction[1] - 1][0] + table[instruction[2] - 1]
    #         table[instruction[1] - 1] = table[instruction[1] - 1][1:]

    # Q2
    for instruction in instructions:
        table[instruction[2] - 1] = table[instruction[1] -
                                          1][:instruction[0]] + table[instruction[2] - 1]
        table[instruction[1] - 1] = table[instruction[1] - 1][instruction[0]:]

    output = ""
    print(table)
    for x in table:
        output += x[0]

    print(output)
