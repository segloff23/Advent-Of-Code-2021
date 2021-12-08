# %% IMPORTS
# import re;
# import math;

# import numpy as np;
# import matplotlib.pyplot as plt;

# from collections import deque;
# from itertools import permutations;

# %% STANDARD READ METHODS
def readIntList():
    with open("problem.txt") as problemFile:
        intList = [int(d) for d in problemFile.readlines()];
    return intList;

def readIntArray(delimiter=" "):
    with open("problem.txt") as problemFile:
        intArray = [[int(d) for d in line.strip().split(delimiter)]
                        for line in problemFile];
    return intArray;

def readWordList():
    with open("problem.txt") as problemFile:
        wordList = [w.strip() for w in problemFile.readlines()];
    return wordList;

def readWordArray(delimiter=" "):
    with open("problem.txt") as problemFile:
        wordArray = [[w.strip() for w in line.strip().split(delimiter)]
                        for line in problemFile];
    return wordArray;

# %% CUSTOM SOLUTION
def readCustom():

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

    depth = 0;
    horz = 0;
    aim = 0;
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

    problem = readCustom();

    partOne(problem);
    partTwo(problem);













