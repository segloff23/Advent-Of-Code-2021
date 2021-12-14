
def read():

    with open("problem.txt") as problemFile:
        problem = [int(x) for x in problemFile.read().strip().split(",")];

    return problem;

def countChildren(number, daysLeft):

    if (number, daysLeft) not in cache:
        if (daysLeft <= 0):
            cache[(number, daysLeft)] = 0;
        else:
            if (number == 0):
                count =  1 + countChildren(0, daysLeft-7) + countChildren(2, daysLeft-7);
            else:
                count = countChildren(0, daysLeft-number);
            cache[(number, daysLeft)] = count;

    return cache[(number, daysLeft)];

def countPopulation(fishes, days):

    numCounts = {};

    for number in range(9):
        count = 1 + countChildren(number, days);
        numCounts[number] = count;

    totalCount = 0;
    for fish in problem:
        totalCount += numCounts[fish];

    return totalCount;

def partOne(problem):

    totalCount = countPopulation(problem, 80)

    print("Part 1: {:d}".format(totalCount));

def partTwo(problem):

    totalCount = countPopulation(problem, 256)

    print("Part 2: {:d}".format(totalCount));

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day 06, AoC 2021");

    cache = {}
    problem = read();

    partOne(problem);
    partTwo(problem);
