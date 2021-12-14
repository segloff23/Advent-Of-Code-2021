
def readWordList():

    with open("problem.txt") as problemFile:
        wordList = [w.strip() for w in problemFile.readlines()];

    return wordList;

def partOne(problem):

    closed = [">", "}", ")", "]"];
    pairs = ["<>", "()", "[]", "{}"];
    points = [25137, 1197, 3, 57];

    goodLines = [];
    total = 0;
    for n, line in enumerate(problem):
        found = True;
        while (found):
            found = False;
            for p in pairs:
                if p in line:
                    found = True;
                    line = line.replace(p, "");
        if (len(line) != 0):
            best = 1e99;
            for c in closed:
                loc = line.find(c);
                if loc != -1 and loc < best:
                    best = loc;
            if best != 1e99:
                char = line[best];
                total += points[closed.index(char)];
            else:
                goodLines.append(problem[n]);
        else:
            goodLines.append(problem[n]);

    print("Part 1: {:d}".format(total));

    return goodLines;

def partTwo(goodLines):

    opens = ["<", "{", "(", "["];
    points = [4, 3, 1, 2];
    pairs = ["<>", "()", "[]", "{}"];

    scores =[];
    for n, line in enumerate(goodLines):
        found = True;
        while (found):
            found = False;
            for p in pairs:
                if p in line:
                    found = True;
                    line = line.replace(p, "");
        if (len(line) != 0):
            subScore = 0;
            for c in reversed(line):
                p = points[opens.index(c)];
                subScore *= 5;
                subScore += p;
            scores.append(subScore);

    scores.sort();
    middle = scores[len(scores) // 2]

    print("Part 2: {:d}".format(middle));

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day 11, AoC 2021");

    problem = readWordList();

    goodLines = partOne(problem);
    partTwo(goodLines);
