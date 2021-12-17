
from heapq import heappush, heappop;

def read():

    with open("problem.txt") as problemFile:
        problem = [[int(x) for x in row.strip()]
                   for row in problemFile.readlines()];

    return problem;

def longFormDijkstra(riskLevels):

    riskLevels = [[-1, *row, -1] for row in riskLevels]
    riskLevels = [[-1]*len(riskLevels[0]), *riskLevels, [-1]*len(riskLevels[0])];

    nR, nC = len(riskLevels), len(riskLevels[0]);

    start = (1, 1);
    end = (nR-2, nC-2);

    piForward, piBackward = {start: 0}, {end: riskLevels[-2][-2]};
    heapForward, heapBackward = [(0, start)], [(riskLevels[-2][-2], end)];
    currentDistForward, currentForward = 0, start;
    currentDistBackward, currentBackward = riskLevels[-2][-2], end;

    while heapForward or heapBackward:

        rF, cF = currentForward;
        rB, cB = currentBackward;

        for rp, cp in ((rF, cF+1), (rF+1, cF), (rF, cF-1), (rF-1, cF)):
            neighbor = (rp, cp);
            cost = riskLevels[rp][cp];
            if (cost != -1):
                dist = currentDistForward + cost;
                if (neighbor not in piForward or dist < piForward[neighbor]):
                    piForward[neighbor] = dist;
                    heappush(heapForward, (dist, neighbor));

        for rp, cp in ((rB, cB+1), (rB+1, cB), (rB, cB-1), (rB-1, cB)):
            neighbor = (rp, cp);
            cost = riskLevels[rp][cp];
            if (cost != -1):
                dist = currentDistBackward + cost;
                if (neighbor not in piBackward or dist < piBackward[neighbor]):
                    piBackward[neighbor] = dist;
                    heappush(heapBackward, (dist, neighbor));

        if (currentForward in piBackward) or (currentBackward in piForward):
            w = min((p for p in piForward if p in piBackward),
                    key = lambda x: piForward[x] + piBackward[x]);
            return piForward[w] + piBackward[w] - riskLevels[w[0]][w[1]];

        riskLevels[rF][cF], riskLevels[rB][cB] = -1, -1;
        currentDistForward, currentForward = heappop(heapForward);
        currentDistBackward, currentBackward = heappop(heapBackward);

    return None;

def partOne(riskLevels):

    risk = longFormDijkstra(riskLevels);
    print("Part 1: {:d}".format(risk));

def partTwo(riskLevels):

    riskLevels = [[x+s if x+s <= 9 else (x+s)%10 + 1 for x in row]
                  for s in range(5) for row in riskLevels];

    riskLevels = [[x+s if x+s <= 9 else (x+s)%10 + 1
                    for s in range(5) for x in row] for row in riskLevels];

    risk = longFormDijkstra(riskLevels);

    print("Part 1: {:d}".format(risk));

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day 15, AoC 2021");

    problem = read();
    partOne(problem);
    partTwo(problem);
