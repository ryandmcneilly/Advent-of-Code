given = """"""


def solution(raw: str):
    raw = raw.split("\n")
    directories = {"/": [0, [], ""]}
    previous_directory = ""
    current_directory = "/"

    raw = raw[1:]
    i = 0
    while i < len(raw):
        line = raw[i]
        if line[:4] == "$ cd":
            if line[-2:] == "..":
                pass
            else:
                current_directory = line[5:]

        if line == "$ ls":
            j = i + 1
            subline = raw[j]
            while j < len(raw) and subline[0] != "$":
                subline = raw[j]
                # Case dir
                if subline[:3] == "dir":
                    directories[subline[4:]] = [0, [], current_directory]
                    directories[current_directory][1].append(subline[4:])

                # Case mem
                if subline.split(" ")[0].isdigit():
                    directories[current_directory][0] += int(
                        subline.split(" ")[0])
                j += 1

        i += 1

    sums = [sum_directory(directories, x)
            for x in directories if sum_directory(directories, x) <= 100000]
    print(directories)
    print(len(sums))


# Now have directories, need to sum
def sum_directory(directory: list, key: str):
    if not directory[key][1]:
        return directory[key][0]

    result = 0
    for i in directory[key][1]:
        result += sum_directory(directory, i)

    return directory[key][0] + result


solution(given)
