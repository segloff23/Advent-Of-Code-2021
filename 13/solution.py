
import re;

def read():

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
    
    return paper;

def partTwo(problem, paper):

    def padRow(row, interval):
        newRow = [];
        for n in range(len(row)):
            if n % interval == 0:
                newRow.extend([0]*3);
            newRow.append(row[n]);

        return newRow;

    _, folds = problem;

    for f in folds[1:]:
        paper = applyFold(paper, f);

    if not FAST:
        from TextConverter import readArrayAsText;
        paperImg = [[255 if x == 0 else 1 for x in row] for row in paper];
        text = readArrayAsText(paperImg);
        print("Part 2: {:s}".format(text));
    else:
        paperImg = ["".join(["@" if x > 0 else " " for x in row]) for row in paper];
        print("Part 2: ");
        for row in paperImg:
            print(row);

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day 13, AoC 2021");

    FAST = True;

    problem = read();

    foldedPaper = partOne(problem);
    partTwo(problem, foldedPaper);
