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
        problem = {};
        for line in problemFile.readlines():
            a, b = line.strip().split("-");
            if a in problem:
                problem[a].append(b);
            else:
                problem[a] = [b];
            if b in problem:
                problem[b].append(a);
            else:
                problem[b] = [a];

    return problem;

def partOne(problem):

    def countPaths(visited, cameFrom, goal):
        
        if (cameFrom == goal):
            return 1;
        else:
            count = 0;
            for n in problem[cameFrom]:
                if n in bigs:
                    count += countPaths(visited, n, goal);
                elif n not in visited:
                    count += countPaths(visited.union({n}), n, goal);
            return count;

    start = "start";
    end = "end";

    bigs = set(loc for loc in problem if loc.isupper())

    count = countPaths({start}, start, end);

    print("Part 1: {:d}".format(count));

def partTwo(problem):

    def countPaths(visited, revisited, cameFrom, goal):
        
        if (cameFrom == goal):
            return 1;
        else:
            count = 0;
            for n in problem[cameFrom]:
                if n in bigs:
                    count += countPaths(visited, revisited, n, goal);
                elif n not in visited:
                    count += countPaths(visited.union({n}), revisited, n, goal);
                elif n != "start" and not revisited:
                    count += countPaths(visited.union({n}), True, n, goal);
            return count;

    bigs = set(loc for loc in problem if loc.isupper())

    start = "start";
    end = "end";

    count = countPaths({start}, False, start, end);

    print("Part 2: {:d}".format(count));

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day 12, AoC 2021");

    problem = readCustom();

    partOne(problem);
    partTwo(problem);













