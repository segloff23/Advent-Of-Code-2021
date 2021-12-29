import sys;

def read():

    with open("problem.txt") as problemFile:
        # pattern = re.compile(r"");
        problem = [];
        for line in problemFile.readlines():
            # m = re.match(pattern, line);
            pass;

    return problem;

def generateSpaceMapping(hallwaySlots, roomSlotMapping):

    # 0  1  2  3  4  5  6  7  8  9 10
    #      11    12    13    14
    #      15    16    17    18
    #      19    20    21    22
    #      23    24    25    26

    mapping = {};
    for h in hallwaySlots:
        for n, L in enumerate(sorted(roomSlotMapping)):
            R = roomSlotMapping[L];
            hL = 2*(n+1);
            low, high = sorted((h, hL));

            spaces = list(range(low, high+1));
            for k, r in enumerate(R):
                spaces = spaces + [r];

                mapping[(h, r)] = spaces;
                mapping[(r, h)] = spaces;

    for n_A, L_A in enumerate(sorted(roomSlotMapping)):
        for n_B, L_B in enumerate(sorted(roomSlotMapping)):
            if (n_A == n_B):
                continue;
            R_A, R_B = roomSlotMapping[L_A], roomSlotMapping[L_B];
            hL_A, hL_B = 2*(n_A+1), 2*(n_B+1);
            low, high = sorted((hL_A, hL_B));

            baseSpaces = list(range(low, high+1));
            for k_A, r_A in enumerate(R_A):
                spaces = baseSpaces + [r for r in R_A[:k_A+1]]
                for k_B, r_B in enumerate(R_B):
                    spaces = spaces + [r_B];
                    mapping[(r_A, r_B)] = spaces;
                    mapping[(r_B, r_A)] = spaces;

    return mapping;

N_R = 4;
costMapping = {"A": 1, "B": 10, "C": 100, "D": 1000}
hallwaySlots = (0, 1, 3, 5, 7, 9, 10);

roomSlotMapping = {L: tuple(n for n in range(k+11, k+11+4*N_R, 4))
                  for k, L in enumerate("ABCD")}
slotOptions = {L: tuple(reversed(roomSlotMapping[L])) + hallwaySlots for L in roomSlotMapping}
spaceMapping = generateSpaceMapping(hallwaySlots, roomSlotMapping);

cache = {tuple(roomSlotMapping[L] for L in "ABCD"): 0};
def DP(subprob, movesMade):

    if (subprob not in cache):
        occupied = set(e for pair in subprob for e in pair);
        costs = [];
        for i, (L, P) in enumerate(zip("ABCD", subprob)):
            roomGoal = roomSlotMapping[L];
            if (P == roomGoal):
                continue;
            for j, p in enumerate(P):

                if p in roomGoal:
                    others = [pAlt for pAlt in occupied if pAlt not in P];
                    shouldMove = False;
                    for oth in others:
                        if oth in roomGoal:
                            shouldMove = True;
                            break;
                    if (not shouldMove):
                        continue;

                for opt in slotOptions[L]:
                    if ((p, opt) not in spaceMapping):
                        continue;

                    if opt in roomGoal:
                        valid = True;
                        for loc in roomGoal:
                            if loc in occupied and loc not in P:
                                valid = False;
                                break;
                        if not valid:
                            continue;
                        elif (p, opt+4) in spaceMapping:
                            if opt+4 not in occupied:
                                continue;

                    spacesToCheck = spaceMapping[(p, opt)];
                    valid = True;
                    for space in spacesToCheck:
                        if space in occupied and space != p:
                            valid = False;
                            break;
                    if (valid):
                        newPair = tuple(sorted(P[:j] + (opt,) + P[j+1:]));
                        newProb = list(subprob);
                        newProb[i] = newPair;
                        newProb = tuple(newProb);
                        c = DP(newProb, movesMade+1) + costMapping[L]*(len(spacesToCheck)-1);
                        costs.append(c);
                        if (c != 1e99 and opt in roomGoal):
                            break;

        if (len(costs) == 0):
            cache[subprob] = 1e99;
        else:
            cache[subprob] = min(costs);

    return cache[subprob]

def partOne(problem):

    # 0  1  2  3  4  5  6  7  8  9 10
    #      11    12    13    14
    #      15    16    17    18
    #      19    20    21    22
    #      23    24    25    26

    # MINE
    subprob = ((12, 18, 21, 24), (13, 17, 20, 23), (14, 16, 22, 26), (11, 15, 19, 25));
    # MINE 2D
    #subprob = ((12, 16), (13, 15), (14, 18), (11, 17));
    # THEIRS
    #subprob = ((18, 21, 23, 26), (11, 13, 17, 20), (12, 16, 22, 25), (14, 15, 19, 24));
    # THEIRS #7 -> FAILS
    #subprob = ((0, 1, 23, 26), (7, 9, 11, 20), (17, 21, 22, 25), (10, 15, 19, 24))
    # THEIRS #12 -> FAILS
    #subprob = ((0, 1, 23, 26), (11, 16, 20, 24), (17, 21, 22, 25), (3, 10, 15, 19))

    # THEIRS #13 -> FAILS
    #subprob = ((0, 1, 23, 26), (11, 16, 20, 24), (13, 17, 21, 25), (3, 10, 15, 19))
    # THEIRS #14 -> WORKS
    #subprob = ((0, 1, 9, 23), (11, 16, 20, 24), (13, 17, 21, 25), (3, 10, 15, 19))

    # THEIRS #17 -> WORKS
    #subprob = ((0, 1, 10, 23), (12, 16, 20, 24), (13, 17, 21, 25), (10, 19, 22, 26))

    cost = DP(subprob, 0);
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
