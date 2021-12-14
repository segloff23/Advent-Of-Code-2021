
def read():

    with open("problem.txt") as problemFile:
        problem = list(problemFile.readlines());

    return problem;

def partOne(problem):

    N = len(problem);
    count = sum([problem[i] > problem[i-1] for i in range(1, N)]);

    print("Part 1: {:d}".format(count));

def partTwo(problem):

    N = len(problem);
    count = sum([problem[i+2] > problem[i-1] for i in range(1, N-2)]);

    print("Part 2: {:d}".format(count));

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day 01, AoC 2021");

    problem = read();

    partOne(problem);
    partTwo(problem);
