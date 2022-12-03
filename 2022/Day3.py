ALPHABET = "abcdefghijklmnopqrstuvwxyz"
def solution(input: str):
    priorities = {}

    for prio, letter in enumerate(ALPHABET + ALPHABET.upper(), start=1):
        priorities[letter] = prio

    data = input.split("\n")

    results = []
    for point in data:
        first, second = point[:len(point)//2], point[len(point)//2:]
        for letter in point:
            if letter in first and letter in second:
                results.append(letter)
                break

    # Q2
    counter = 0
    q2 = []
    for r in range(0, len(data) - 2, 3):
        for letter in ALPHABET + ALPHABET.upper():
            if letter in data[r] and letter in data[r + 1] and letter in data[r + 2]:
                q2.append(letter)
                break

    # Q1
    sum = 0
    for result in results:
        sum += priorities[result]
    print(sum)

    # Q2
    sum = 0
    for result in q2:
        sum += priorities[result]
    print(sum)