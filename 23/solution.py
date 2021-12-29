# %% IMPORTS
# import re;
# import math;

# import numpy as np;
# import matplotlib.pyplot as plt;

# from collections import deque;
# from itertools import permutations;

def read():

    with open("problem.txt") as problemFile:
        # pattern = re.compile(r"");
        problem = [];
        for line in problemFile.readlines():
            # m = re.match(pattern, line);
            pass;

    return problem;

# 0  1  2  3  4  5  6  7  8  9 10
#      11    12    13    14
#      15    16    17    18

options = {"A": (0, 1, 3, 5, 7, 9, 10, 11, 15),
           "B": (0, 1, 3, 5, 7, 9, 10, 12, 16),
           "C": (0, 1, 3, 5, 7, 9, 10, 13, 17),
           "D": (0, 1, 3, 5, 7, 9, 10, 14, 18)}

hallway = [0, 1, 3, 5, 7, 9, 10];
rooms = [[11, 15], [12, 16], [13, 17], [14, 18]];

fullMap = {};
for h in hallway:
    for n, (r1, r2) in enumerate(rooms):
        hA = 2*(n+1)

        baseCost = abs(h - hA);
        high, low = max((h, hA)), min((h, hA));
        baseRange = list(range(low, high+1));

        h_r1 = {"cost": baseCost + 1, "spaces": baseRange + [r1]}
        fullMap[(h, r1)] = h_r1;
        fullMap[(r1, h)] = h_r1;

        h_r2 = {"cost": baseCost + 2, "spaces": baseRange + [r1, r2]}
        fullMap[(h, r2)] = h_r2;
        fullMap[(r2, h)] = h_r2;

for n_A, (r1_A, r2_A) in enumerate(rooms):
    h_A = 2*(n_A+1);
    for n_B, (r1_B, r2_B) in enumerate(rooms):
        if n_A != n_B:
            h_B = 2*(n_B+1)
            baseCost = abs(h_A - h_B);
            high, low = max((h_A, h_B)), min((h_A, h_B));
            baseRange = list(range(low, high+1));

            r1_A_r1_B = {"cost": baseCost + 2, "spaces": baseRange + [r1_A, r1_B]}
            fullMap[(r1_A, r1_B)] = r1_A_r1_B;
            fullMap[(r1_B, r1_A)] = r1_A_r1_B;

            r1_A_r2_B = {"cost": baseCost + 3, "spaces": baseRange + [r1_A, r1_B, r2_B]}
            fullMap[(r1_A, r2_B)] = r1_A_r2_B;
            fullMap[(r2_B, r1_A)] = r1_A_r2_B;

            r2_A_r1_B = {"cost": baseCost + 3, "spaces": baseRange + [r1_A, r2_A, r1_B]}
            fullMap[(r2_A, r1_B)] = r2_A_r1_B;
            fullMap[(r1_B, r2_A)] = r2_A_r1_B;

            r2_A_r2_B = {"cost": baseCost + 4, "spaces": baseRange + [r1_A, r2_A, r1_B, r2_B]}
            fullMap[(r2_A, r2_B)] = r2_A_r2_B;
            fullMap[(r2_B, r2_A)] = r2_A_r2_B;

costMap = {"A": 1, "B": 10, "C": 100, "D": 1000}

goalMap = {"A": (11, 15), "B": (12, 16), "C": (13, 17), "D": (14, 18)}

COUNT = [0];
cache = {};
def DP(subproblem,):

    if subproblem not in cache:

        if subproblem == ((11, 15), (12, 16), (13, 17), (14, 18)):
            cache[subproblem] = 0;
        else:
            costs = [];
            occupied = set(e for pair in subproblem for e in pair );
            for n, (L, (p1, p2)) in enumerate(zip("ABCD", subproblem)):
                opts = options[L];
                if (p1, p2) == goalMap[L]:
                    continue;
                for o in opts:
                    if ((p1, o) not in fullMap):
                        continue;
                    
                    if p1 in goalMap[L]:
                        temp = list(goalMap[L])
                        temp.remove(p1)
                        other = temp[0];
                        if other not in occupied:
                            continue;
                    
                    if o == goalMap[L][0]:
                        if goalMap[L][1] != p2:
                            continue;
                    
                    move = fullMap[(p1, o)];
                    valid = True;
                    for space in move["spaces"]:
                        if space in occupied and space != p1:
                            valid = False;
                            break;
                    if (valid):
                        if o > p2:
                            newPair = (p2, o);
                        else:
                            newPair = (o, p2);
                        newProb = list(subproblem);
                        newProb[n] = newPair;
                        newProb = tuple(newProb);
                        costs.append(DP(newProb) + costMap[L]*move["cost"]);

                for o in opts:
                    if ((p2, o) not in fullMap):
                        continue;
                    
                    if p2 in goalMap[L]:
                        temp = list(goalMap[L])
                        temp.remove(p2)
                        other = temp[0];
                        if other not in occupied:
                            continue;
                    
                    if o == goalMap[L][0]:
                        if goalMap[L][1] != p1:
                            continue;

                    move = fullMap[(p2, o)];
                    valid = True;
                    for space in move["spaces"]:
                        if space in occupied and space != p2:
                            valid = False;
                            break;
                    if (valid):
                        if o > p1:
                            newPair = (p1, o);
                        else:
                            newPair = (o, p1);
                        newProb = list(subproblem);
                        newProb[n] = newPair;
                        newProb = tuple(newProb);
                        costs.append(DP(newProb) + costMap[L]*move["cost"]);

            if (len(costs) == 0):
                cache[subproblem] = 1e99;
            else:
                cache[subproblem] = min(costs);

    return cache[subproblem];

def partOne(problem):

# 0  1  2  3  4  5  6  7  8  9 10
#      11    12    13    14
#      15    16    17    18

    #############
    #...........#
    ###D#A#B#C###
      #B#A#D#C#
      #########

    subprob = ((12, 16), (13, 15), (14, 18), (11, 17));
    
    cost = DP(subprob);
    
    print(cost);
    

    print("Part 1: {:d}".format(0));

    return 0;

def partTwo(problem, partOneOutput):

    print("Part 2: {:d}".format(0));

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day 23, AoC 2021");

    problem = read();
    partOneOutput = partOne(problem);
    partTwo(problem, partOneOutput);
