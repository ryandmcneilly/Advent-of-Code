def read_input(dayNum, seperator='\n'):
    fileName = f"./day{dayNum}.in"
    inFile = open(fileName, 'r')
    lines = inFile.read().split(seperator)
    inFile.close()
    return lines[:-1] # Cuts null last element

def get_colour(xs):
    output = [0, 0, 0] #rgb
    for x in xs:
        if x[-4:] == "blue":
            output[2] = int(x.replace(" ", "")[:-4])
        if x[-5:] == "green":
            output[1] = int(x.replace(" ", "")[:-5])
        if x[-3:] == "red":
            output[0] = int(x.replace(" ", "")[:-3])

    return output


     

def main():
    data = read_input(2)

    # Part 1
    RED_LIMIT = 12
    GREEN_LIMIT = 13
    BLUE_LIMIT = 14
    LIMITS = [RED_LIMIT, GREEN_LIMIT, BLUE_LIMIT]

    data = [xs.split(':')[1] for xs in data]
    data = [xs.split(';') for xs in data]
    data = [[x.split(',') for x in xs] for xs in data]
    data = [[get_colour(x) for x in xs] for xs in data]
   
    # Biggest color value for each part
    data = [[max(xs, key=lambda x: x[0])[0], max(xs, key=lambda x: x[1])[1], max(xs, key=lambda x: x[2])[2]] for xs in data] 

    data = [[xs[0] <= RED_LIMIT, xs[1] <= GREEN_LIMIT, xs[2] <= BLUE_LIMIT] for xs in data]

    data = sum([idx + 1 for idx, xs in enumerate(data) if all(xs)])


    


    print(data)



if __name__ == "__main__":
    main()
