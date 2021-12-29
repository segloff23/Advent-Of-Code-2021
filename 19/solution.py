# %% IMPORTS
# import re;
# import math;

# import numpy as np;
# import matplotlib.pyplot as plt;

# from collections import deque;
# from itertools import permutations;

def read():

    with open("problem.txt") as problemFile:
        problem = [[[int(x) for x in line.split(",")]
                    for line in scanner.split("\n")[1:]]
                   for scanner in problemFile.read().split("\n\n")];

    return problem;

def rotate90(v, axis, k=1):

    if axis == 0:
        for n in range(k):
            v = [v[0], -v[2], v[1]];
    elif axis == 1:
        for n in range(k):
            v = [v[2], v[1], -v[0]];
    elif axis == 2:
        for n in range(k):
            v = [-v[1], v[0], v[2]];

    return v;

def transform(scanner, R, T):
    
    for r, k_r in enumerate(R):
        if k_r != 0:
            scanner = [rotate90(A, r, k=k_r) for A in scanner];
    return [[a+t for a,t in zip(A, T)] for A in scanner];

def matchScanners(scannerA, scannerB):

    B_x = scannerB;
    for k_x in range(4):
        B_xz = B_x;
        for k_z in range(4):
            diff, new = countMatches(scannerA, B_xz);
            if diff:
                return ([k_x, 0, k_z], diff), new;
            B_xz = [rotate90(B, 2) for B in B_xz];
        B_x = [rotate90(B, 0) for B in B_x];

    B_y = [rotate90(B, 1) for B in scannerB]
    for k_y in [1, 3]:
        B_yz = B_y;
        for k_z in range(4):
            diff, new = countMatches(scannerA, B_yz);
            if diff:
                return ([0, k_y, k_z], diff), new;
            B_yz = [rotate90(B, 2) for B in B_yz];
        B_y = [rotate90(B, 0, k=2) for B in B_y];

    return None, None;

def countMatches(scannerA, scannerB):

    scannerA = sorted(scannerA);
    scannerB = sorted(scannerB);
    
    for targetA in scannerA:
        for targetB in scannerB[:-11]:            
            diff = [a-b for a,b in zip(targetA, targetB)];
            matches = sum([b+d for b,d in zip(B, diff)] in scannerA
                          for B in scannerB);
            if matches >= 12:
                return diff, [[b+d for b,d in zip(B, diff)] for B in scannerB];

    return None, None;

def partOne(problem):

    mappings = {0: ([0, 0, 0], [0, 0, 0])}
    known = [0];
    visited = set();

    while len(mappings) < len(problem):
        target = known.pop();
        if target not in visited:
            A = problem[target];
            for n, B in enumerate(problem):
                if (n != target and n not in known and n not in visited):
                    diff, new = matchScanners(A, B);
                    if (diff):
                        mappings[n] = diff;
                        known.append(n);
                        problem[n] = new;
            visited.add(target);

    beacons = set();
    for scanner in problem:
        for b in scanner:
            beacons.add(tuple(b));
    count = len(beacons)

    print("Part 1: {:d}".format(count));

    return mappings;

def partTwo(problem, partOneOutput):

    distances = [partOneOutput[n][1] for n in partOneOutput];
    
    largest = 0;
    for nA in range(len(distances)):
        dA = distances[nA];
        for nB in range(nA+1, len(distances)):
            dB = distances[nB];
            total = sum(abs(a-b) for a,b in zip(dA, dB));
            if total > largest:
                largest = total;
    
    print("Part 2: {:d}".format(largest));

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day 19, AoC 2021");

    problem = read();
    partOneOutput = partOne(problem);
    partTwo(problem, partOneOutput);
