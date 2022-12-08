def solution(raw: str):
    raw = raw.split("\n")

    for r in range(0, len(raw)):
        raw[r] = [int(i) for i in raw[r]]

    print(raw)
    tranpose = list(map(list, zip(*raw)))

    # Slow brute force !!
    count = 0
    products = []
    for j in range(1, len(raw) - 1):
        for i in range(1, len(raw[0]) - 1):
            # Check row and column
            if (max(raw[j][:i]) < raw[j][i] or
                max(raw[j][i+1:]) < raw[j][i] or
                max(tranpose[i][:j]) < raw[j][i] or
                    max(tranpose[i][j+1:]) < raw[j][i]):
                count += 1

            # Q2
            result = []
            result.append(forward(raw[j][:i][::-1], raw[j][i]))
            result.append(forward(raw[j][i+1:], raw[j][i]))
            result.append(forward(tranpose[i][:j][::-1], raw[j][i]))
            result.append(forward(tranpose[i][j+1:], raw[j][i]))

            product = 1
            for k in result:
                product *= k
            products.append(product)

    # Add amount of exterior trees
    count += len(raw) * len(raw[0]) - ((len(raw) - 2) * (len(raw[0]) - 2))

    # Q1
    print(count)
    # Q2
    print(max(products))

# Helper function to get the viewing distance
def forward(array: list, origin: int) -> int:
    counter = 0
    while array:
        if array.pop(0) >= origin:
            return counter + 1
        counter += 1
    return counter