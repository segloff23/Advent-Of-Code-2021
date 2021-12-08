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
        problem = list(problemFile.readlines());

    return problem;

def partOne(problem):
    
    count = sum([problem[i] > problem[i-1] for i in range(1, len(problem))]);

    print("Part 1: {:d}".format(count));

def partTwo(problem):

    count = sum([problem[i+2] > problem[i-1] for i in range(1, len(problem)-2)]);

    print("Part 2: {:d}".format(count));

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day 01, AoC 2021");

    problem = readIntList();

    partOne(problem);
    partTwo(problem);
