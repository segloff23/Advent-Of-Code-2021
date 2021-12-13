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

    problem = readCustom();

    partOne(problem);
    partTwo(problem);



