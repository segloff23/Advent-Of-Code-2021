# %% IMPORTS
# import re;
# import math;

# import numpy as np;
# import matplotlib.pyplot as plt;

# from collections import deque;
# from itertools import permutations;

def read():

    with open("problem.txt") as problemFile:
        problem = [w.strip() for w in problemFile.readlines()];

    return problem;

def partOne(problem):

    N_R, N_C = len(problem), len(problem[0]);

    mapping = {">": 1, "v": -1, ".": 0}
    cucumbers = [[mapping[c] for c in row] for row in problem]

    eastFacing = [[r, c] for r in range(N_R) for c in range(N_C) if cucumbers[r][c] == 1];
    southFacing = [[r, c] for r in range(N_R) for c in range(N_C) if cucumbers[r][c] == -1];

    movesMade = 0;
    moved = True;
    while (moved):

        moved = False;
        movesMade += 1;

        newCucumbers = [[0]*N_C for r in range(N_R)];
        for n, (r, c) in enumerate(eastFacing):
            cp = (c+1)%N_C;
            if cucumbers[r][cp] == 0:
                newCucumbers[r][cp] = 1;
                eastFacing[n][1] = cp;
                moved = True;
            else:
                newCucumbers[r][c] = 1;
        for n, (r, c) in enumerate(southFacing):
            rp = (r+1)%N_R;
            if cucumbers[rp][c] != -1 and newCucumbers[rp][c] == 0:
                newCucumbers[rp][c] = -1;
                southFacing[n][0] = rp;
                moved = True;
            else:
                newCucumbers[r][c] = -1;
        cucumbers = newCucumbers;

    print("Part 1: {:d}".format(movesMade));

    return 0;

def partTwo(problem, partOneOutput):

    print("Part 2: {:s}".format("All 50 stars completed!"));

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day 25, AoC 2021");

    problem = read();
    partOneOutput = partOne(problem);
    partTwo(problem, partOneOutput);
