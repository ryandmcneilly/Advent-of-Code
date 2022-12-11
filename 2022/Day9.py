def solution(raw: str):
    raw = raw.split("\n")

    # (0, 0) is bottom left
    head = [0, 0]
    tail = [0, 0]

    visited = [[0, 0]]

    directions = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

    # [2, 1], [0, 0]

    for i in raw:
        direction, mag = i.split(" ")
        mag = int(mag)

        # Deal with head
        head[0] += directions[direction][0] * mag
        head[1] += directions[direction][1] * mag

        while not (abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1):
            if (abs(head[0] - tail[0]) >= 1) and (abs(head[1] - tail[1]) > 1):
                tail[0] += (1 if head[0] > tail[0] else -1)
                tail[1] += (1 if head[1] > tail[1] else -1)

            elif (abs(head[1] - tail[1]) >= 1) and (abs(head[0] - tail[0]) > 1):
                tail[0] += (1 if head[0] > tail[0] else -1)
                tail[1] += (1 if head[1] > tail[1] else -1)

            # Tail two steps away horizontal
            elif abs(head[0] - tail[0]) >= 2:
                tail[0] += (1 if head[0] > tail[0] else -1)

            # Tail two steps away vertical
            elif abs(head[1] - tail[1]) >= 2:
                tail[1] += (1 if head[1] > tail[1] else -1)

            visited.append([tail[0], tail[1]])

    b_set = set(tuple(x) for x in visited)
    visited = [list(x) for x in b_set]
    # print(len(visited))


def solution2(raw: str):

    # (0, 0) is bottom left

    rope = [[0, 0]] * 10
    print(rope)

    directions = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

    visited = {[0, 0]}

    for line in raw.split("\n"):
        d, m = line
        d = directions[d]

        for r in range(1, int(m)):
            ropex, ropey = rope[r]
            movex, movey = rope[r - 1][0] - ropex, rope[r - 1][1] - ropey

            if abs(movex) > 1 or abs(movey) > 1:
                if movex != 0:
                    ropex += 1 if movex > 0 else -1
                if movey != 0:
                    ropey += 1 if movey > 0 else -1

        rope[r] = [ropex, ropey]

    print(visited)
    b_set = set(tuple(x) for x in visited)
    visited = [list(x) for x in b_set]
    print(len(visited))


solution2(given)
