from heapq import heappop, heappush;

def read():

    with open("problem.txt") as problemFile:
        problem = [[int(x) for x in row.strip()]
                   for row in problemFile.readlines()]

    return problem;

# Slightly sped up version of following:
# https://www.reddit.com/r/adventofcode/comments/rgqzt5/2021_day_15_solutions/hom70ua/
def calcRisks(m):

    m = [[-1] + row + [-1] for row in m];
    m = [[-1]*len(m[0])] + m + [[-1]*len(m[0])];

    h, w = len(m), len(m[0]);

    end = (w-2, h-2);
    heap = [(0,(1,1))];
    while heap:
        risk, node = heappop(heap);
        if node == end:
            return risk;
        x0, y0 = node;
        for x, y in ((x0, y0+1), (x0+1, y0), (x0, y0-1), (x0-1, y0)):
            if m[y][x] >= 0:
                heappush(heap, (risk+m[y][x], (x,y)));
                m[y][x] = -1;

    return None;

def partOne(riskLevels):

    risk = calcRisks(riskLevels);
    print("Part 1: {:d}".format(risk));

def partTwo(riskLevels, partOneOutput):

    riskLevels = [[x+s if x+s <= 9 else (x+s)%10 + 1 for x in row]
                  for s in range(5) for row in riskLevels];

    riskLevels = [[x+s if x+s <= 9 else (x+s)%10 + 1
                    for s in range(5) for x in row] for row in riskLevels];

    risk = calcRisks(riskLevels);

    print("Part 2: {:d}".format(risk));

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day 15, AoC 2021");

    problem = read();
    partOneOutput = partOne(problem)
    partTwo(problem, partOneOutput);
