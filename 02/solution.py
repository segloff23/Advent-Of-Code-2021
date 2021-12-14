
def read():

    with open("problem.txt") as problemFile:
        problem = [];
        for line in problemFile.readlines():
            x, y = line.split(" ");
            problem.append([x, int(y)]);

    return problem;

def partOne(problem):

    direc = {"forward": 1+0j, "down": 1j, "up": -1j}

    pos = 0+0j;
    for move, dist in problem:
        pos += dist * direc[move];

    result = int(pos.real) * int(pos.imag);

    print("Part 1: {:d}".format(result));

def partTwo(problem):

    depth, horz, aim = 0, 0, 0;
    for move, dist in problem:
        if (move == "forward"):
            horz += dist;
            depth += aim * dist;
        elif (move == "down"):
            aim += dist;
        elif (move == "up"):
            aim -= dist;

    result = depth * horz;

    print("Part 2: {:d}".format(result));

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day 02, AoC 2021");

    problem = read();

    partOne(problem);
    partTwo(problem);
