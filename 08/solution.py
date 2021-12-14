
from itertools import permutations;

def read():

    with open("problem.txt") as problemFile:
        problem = [];
        for line in problemFile.readlines():
            samplesRaw, outputRaw = line.split(" | ");
            samples = ["".join(sorted(x)) for x in samplesRaw.strip().split(" ")];
            output =["".join(sorted(x)) for x in outputRaw.strip().split(" ")];
            problem.append((samples, output));

    return problem;

def partOne(problem):

    count = 0;
    lengths = set([2, 4, 3, 7]);
    for _, out in problem:
        for letter in out:
            L = len(letter);
            if L in lengths:
                count += 1;

    print("Part 1: {:d}".format(count));

def partTwo(problem):

    valids = {"abcefg": "0", "cf": "1", "acdeg": "2", "acdfg": "3",
              "bcdf": "4", "abdfg": "5", "abdefg": "6", "acf": "7",
              "abcdefg": "8", "abcdfg": "9"};

    def swap(key, perm):
        return "".join(sorted(perm[c] for c in key));

    fullString = "abcdefg";

    perms = [];
    permsBackward = [];
    matchers = [];
    for p in permutations(fullString):
        permsBackward.append({fullString[i]: p[i] for i in range(len(p))});
        perms.append({p[i]: fullString[i] for i in range(len(p))});
        matchers.append(set(swap(x, perms[-1]) for x in valids));

    total = 0;
    for sample, outs in problem:
        mapping = None;
        for perm, permBack, match in zip(perms, permsBackward, matchers):
            validPerm = True;
            for s in sample:
                if s not in match:
                    validPerm = False;
                    break;
            if (validPerm):
                mapping = permBack;
                break;
        if (not validPerm):
            print("uh oh");
        total += int("".join(valids[swap(d, mapping)] for d in outs));

    print("Part 2: {:d}".format(total));

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day 08, AoC 2021");

    problem = read();

    partOne(problem);
    partTwo(problem);
