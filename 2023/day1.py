def read_input(dayNum, seperator='\n'):
    fileName = f"./day{dayNum}.in"
    inFile = open(fileName, 'r')
    lines = inFile.read().split(seperator)
    inFile.close()
    return lines[:-1] # Cuts null last element

def main():
    xss = read_input(1)
    
    # Part two
    numMap = {
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9',
    }

    # replacing first and last value 
    for i in range(len(xss)):
        # find the first number
        acc = ""
        found = False
        for j in range(len(xss[i])):
            if '0' <= xss[i][j] and xss[i][j] <= '9':
                break
            acc += xss[i][j]
            for spelling in numMap:
                if spelling in acc:
                    acc = acc.replace(spelling, numMap[spelling])
                    xss[i] = acc + xss[i][j+1:]
                    found = True
                    break
            
            if found:
                break
       
        # find the last number
        acc = ""
        found = False
        for j in range(len(xss[i]) - 1, -1, -1):
            if '0' <= xss[i][j] and xss[i][j] <= '9':
                break
            acc = xss[i][j] + acc
            for spelling in numMap:
                if spelling in acc:
                    acc = acc.replace(spelling, numMap[spelling])
                    xss[i] = xss[i][:j] + acc
                    found = True
            
            if found:
                break

    # Part One
    xs = [[x for x in xs if '0' <= x and x <= '9'] for xs in xss]
    xs = [int(f"{x[0]}{x[-1]}") for x in xs]
    print(sum(xs))
    
    


if __name__ == "__main__":
    main()
