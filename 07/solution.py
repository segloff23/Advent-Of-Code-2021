
def read():

    with open("problem.txt") as problemFile:
        problem = [int(x) for x in problemFile.read().strip().split(",")];

    start = min(problem);
    stop = max(problem);

    return problem, start, stop;

def partOne(problem):

    def cost(x, y):
        return abs(x - y);

    data, start, stop = problem;

    minCost = sum(cost(x, start) for x in data);

    for pos in range(start+1, stop+1):
        trialCost = sum(cost(x, pos) for x in data);
        if (trialCost < minCost):
            minCost = trialCost;
        else:
            break;

    print("Part 1: {:d}".format(minCost));

def partTwo(problem):

    def cost(x, y):
        diff = abs(x - y);
        return diff * (diff + 1) // 2;

    data, start, stop = problem;

    minCost = sum(cost(x, start) for x in data);

    for pos in range(start+1, stop+1):
        trialCost = sum(cost(x, pos) for x in data);
        if (trialCost < minCost):
            minCost = trialCost;
        else:
            break;

    print("Part 2: {:d}".format(minCost));

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day 07, AoC 2021");

    problem = read();

    partOne(problem);
    partTwo(problem);
