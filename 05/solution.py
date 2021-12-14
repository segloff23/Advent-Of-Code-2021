
import re;

def read():

    with open("problem.txt") as problemFile:
        patternStr = r"(?P<x1>\d+),(?P<y1>\d+) -> (?P<x2>\d+),(?P<y2>\d+)";
        pattern = re.compile(patternStr);
        problem = [];
        for line in problemFile.readlines():
            m = re.match(pattern, line);
            X = (int(m.group("x1")), int(m.group("x2")));
            Y = (int(m.group("y1")), int(m.group("y2")));
            problem.append((X, Y));

    xSet = [x for X, _ in problem for x in X];
    ySet = [y for _, Y in problem for y in Y];

    minX, maxX = min(xSet), max(xSet);
    minY, maxY = min(ySet), max(ySet);
    xRange, yRange = maxX - minX + 1, maxY - minY + 1;

    return [problem, minX, minY, xRange, yRange];

def partOne(problem):

    data, minX, minY, xRange, yRange = problem;

    mapping = [[0]*xRange for _ in range(yRange)];
    for X, Y in data:
        if X[0] == X[1]:
            start, stop = sorted(Y);
            for y in range(start, stop+1):
                mapping[y-minY][X[0]-minX] += 1;
        elif Y[0] == Y[1]:
            start, stop = sorted(X);
            for x in range(start, stop+1):
                mapping[Y[0]-minY][x-minX] += 1;

    count = sum(1 for row in mapping for e in row if e > 1);

    print("Part 1: {:d}".format(count));

def partTwo(problem):

    data, minX, minY, xRange, yRange = problem;

    mapping = [[0]*xRange for _ in range(yRange)];
    for X, Y in data:
        xSign = 0 if X[1] == X[0] else 1 if X[1] > X[0] else -1;
        ySign = 0 if Y[1] == Y[0] else 1 if Y[1] > Y[0] else -1;
        x, y = X[0], Y[0];
        while x != X[1] or y != Y[1]:
            mapping[y-minY][x-minX] += 1;
            x += xSign;
            y += ySign;
        mapping[y-minY][x-minX] += 1;

    count = sum(1 for row in mapping for e in row if e > 1);

    print("Part 2: {:d}".format(count));

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day 05, AoC 2021");

    problem = read();

    partOne(problem);
    partTwo(problem);
