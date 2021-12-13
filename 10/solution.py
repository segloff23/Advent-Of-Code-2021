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
        # pattern = re.compile(r"");
        problem = [];
        for line in problemFile.readlines():
            # m = re.match(pattern, line);
            pass;

    return problem;

def partOne(problem):

    pairs = ["()", "[]", "{}", "<>"];
    points = [3, 57, 1197, 25137];

    validLines = [];
    score = 0;
    for line in problem:

        oldLength = len(line);
        found = True;
        while found:
            for p in pairs:
                line = line.replace(p, "");
            if len(line) == oldLength:
                found = False;
            else:
                oldLength = len(line);
        minIndex = -1;
        for opener, closer in pairs:
            if closer in line:
                index = line.index(closer);
                if index < minIndex or minIndex == -1:
                    minIndex = index;
        if (minIndex != -1):
            symbol = line[minIndex];
            for n, p in enumerate(pairs):
                if symbol in p:
                    score += points[n];
                    break;
        else:
            validLines.append(line);

    print("Part 1: {:d}".format(score));

    return validLines;

def partTwo(validLines):

    points = {"(": 1, "[": 2, "{": 3, "<": 4}

    scores = [];
    for line in validLines:
        score = 0;
        for c in reversed(line):
            score *= 5;
            score += points[c];
        scores.append(score);

    scores.sort();
    winner = scores[len(scores)//2]

    print("Part 2: {:d}".format(winner));

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day 10, AoC 2021");

    problem = readWordList();

    validLines = partOne(problem);
    partTwo(validLines);













