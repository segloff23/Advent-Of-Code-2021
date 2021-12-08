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
        start = [int(x) for x in problemFile.readline().strip().split(",")];
        data = [line.strip().split("\n") for line in problemFile.read().split("\n\n")];
        boardsRaw = [[row.split(" ") for row in line] for line in data];
        boards = [];
        for b in boardsRaw:
            board = [];
            for row in b:
                board.append([int(x) for x in row if x != ""]);
            boards.append(board);

    return [start, boards];

def hasWon(board):
    
    for row in board:
        if row.count(1) == len(row):
            return True;
    
    colCounts = [[row[i] for row in board].count(1) for i in range(len(row))];
    for c in colCounts:
        if c == len(row):
            return True;
    
    return False;

def countUnmarked(board, boardState):
    total = 0;
    N = len(board);
    
    for r in range(N):
        for c in range(N):
            if (boardState[r][c] == 0):
                total += board[r][c];
    
    return total;
    

def partOne(problem):
    
    numbers, boards = problem;
    
    N = len(boards[0]);
    
    boardStates = [];
    for b in boards:
        boardStates.append([[0]*N for b in range(N)]);

    for num in numbers:
        for n, b in enumerate(boards):
            for row in range(N):
                for col in range(N):
                    if b[row][col] == num:
                        boardStates[n][row][col] = 1;
            if (hasWon(boardStates[n])):
                break;
        if (hasWon(boardStates[n])):
            break;
    
    total = countUnmarked(boards[n], boardStates[n]);
    lastCall = num;
    
    product = total * lastCall;

    print("Part 1: {:d}".format(product));

def partTwo(problem):
    
    numbers, boards = problem;
    
    N = len(boards[0]);
    
    boardStates = [];
    for b in boards:
        boardStates.append([[0]*N for b in range(N)]);

    numWinners = 0;
    alreadyWon = set();
    for kn, num in enumerate(numbers):
        
        for n, b in enumerate(boards):
            for row in range(N):
                for col in range(N):
                    if b[row][col] == num:
                        boardStates[n][row][col] = 1;
            if (hasWon(boardStates[n])):
                if n not in alreadyWon:
                    numWinners += 1;
                    alreadyWon.add(n);
                    if numWinners == len(boards) - 1:
                        break;
        if numWinners == len(boards) - 1:
            break;

    tar = 0;
    for n, b in enumerate(boards):
        if (not hasWon(boardStates[n])):
            tar = n;
            break;

    tarNum = 0;

    for num in numbers[kn:]:
        for row in range(N):
            for col in range(N):
                if b[row][col] == num:
                    boardStates[tar][row][col] = 1;
        if (hasWon(boardStates[tar])):
            tarNum = num;
            break;
            
    product = tarNum * countUnmarked(boards[tar], boardStates[tar]);
    print("Part 2: {:d}".format(product));

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day 02, AoC 2021");

    problem = readCustom();

    partOne(problem);
    partTwo(problem);













