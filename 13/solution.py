# %% IMPORTS
import re;
# import math;

#import numpy as np;
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
        nums, words = problemFile.read().split("\n\n");

        coords = [];
        for line in nums.strip().split("\n"):
            coords.append([int(x) for x in line.strip().split(",")]);

        folds = [];
        pattern = re.compile(r"fold along (\w)=(\d+)");
        for line in words.strip().split("\n"):
            m = re.match(pattern, line);
            folds.append((m.group(1), int(m.group(2))));

        problem = [coords, folds];

    return problem;

def applyFold(paper, fold):

    NR, NC = len(paper), len(paper[0]);
    direction, z = fold;

    if direction == "y":
        start, stop = z+1, min(z+1+z, NR);
        nR = stop - start;
        for r, rF in zip(range(z-nR, z), range(stop-1, start-1, -1)):
            for c in range(NC):
               paper[r][c] += paper[rF][c];
        paper = paper[:z];
    elif direction == "x":
        start, stop = z+1, min(z+1+z, NC);
        nC = stop - start;
        for c, cF in zip(range(z-nC, z), range(stop-1, start-1, -1)):
            for r in range(NR):
                paper[r][c] += paper[r][cF];
        paper = [row[:z] for row in paper];

    return paper;

def partOne(problem):

    coords, folds = problem;

    high = max(x for row in coords for x in row);
    N = high + 1;

    paper = [[0]*N for _ in range(N)];
    for x, y in coords:
        paper[y][x] += 1;

    paper = applyFold(paper, folds[0]);
    total = sum(x != 0 for row in paper for x in row);

    print("Part 1: {:d}".format(total));

def partTwo(problem):

    coords, folds = problem;

    high = max(x for row in coords for x in row);
    N = high + 1;

    paper = [[0]*N for _ in range(N)];
    for x, y in coords:
        paper[y][x] += 1;

    for f in folds:
        paper = applyFold(paper, f);

    message = [""]*len(paper);
    for n, row in enumerate(paper):
        for x in row:
            message[n] += "#" if x != 0 else " ";



    print("Part 2: ");
    for row in message:
        print(" "*8 + row);

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day 13, AoC 2021");

    problem = readCustom();

    partOne(problem);
    partTwo(problem);













