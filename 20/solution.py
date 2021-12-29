
def read():

    with open("problem.txt") as problemFile:
        decoder, rest = problemFile.read().split("\n\n");
        image = [line.strip() for line in rest.split("\n")];

    return decoder.strip(), image;

def enhance(image, decoder):

    N_R, N_C = len(image), len(image[0]);
    
    newImage = [[*row] for row in image];

    for i in range(1, N_R-1):
        for j in range(1, N_C-1):
            code = "".join("".join(row[j-1:j+2]) for row in image[i-1:i+2]);
            index = int("0b"+code, 2);

            newImage[i][j] = decoder[index];

    return newImage;

def partOne(problem):

    decoder, image = problem;

    image = [["1" if x=="#" else "0" for x in row] for row in image];
    decoder = ["1" if x=="#" else "0" for x in decoder];

    padding = 5;

    for n in range(25):
        N_C = len(image[0]);
        image = [["0"]*N_C for n in range(padding)] + image + [["0"]*N_C for n in range(padding)];
        image = [["0"]*padding + row + ["0"]*padding for row in image];
    
        for k in range(2):
            image = enhance(image, decoder);
        
        image = [row[2:-2] for row in image[2:-2]];
        print(n);

    # for row in image:
    #     print("".join(row));

    totalLit = sum(row[2:-2].count("1") for row in image[2:-2]);

    print("Part 1: {:d}".format(totalLit));

    return 0;

def partTwo(problem, partOneOutput):

    print("Part 2: {:d}".format(0));

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day 20, AoC 2021");

    problem = read();
    partOneOutput = partOne(problem);
    partTwo(problem, partOneOutput);

# 5035 TOO HIGH
# 5033 TOO HIGH