#%% github solution
# from heapq import heappop, heappush;

# def read():

#     with open("problem.txt") as problemFile:
#         problem = [[int(x) for x in row.strip()]
#                    for row in problemFile.readlines()]

#     return problem;

# # Slightly sped up version of following:
# # https://www.reddit.com/r/adventofcode/comments/rgqzt5/2021_day_15_solutions/hom70ua/
# def calcRisks(m):

#     m = [[-1] + row + [-1] for row in m];
#     m = [[-1]*len(m[0])] + m + [[-1]*len(m[0])];

#     h, w = len(m), len(m[0]);

#     end = (w-2, h-2);
#     heap = [(0,(1,1))];
#     while heap:
#         risk, node = heappop(heap);
#         if node == end:
#             return risk;
#         x0, y0 = node;
#         for x, y in ((x0, y0+1), (x0+1, y0), (x0, y0-1), (x0-1, y0)):
#             if m[y][x] >= 0:
#                 heappush(heap, (risk+m[y][x], (x,y)));
#                 m[y][x] = -1;

#     return None;

# def partOne(riskLevels):

#     risk = calcRisks(riskLevels);
#     print("Part 1: {:d}".format(risk));

# def partTwo(riskLevels, partOneOutput):

#     riskLevels = [[x+s if x+s <= 9 else (x+s)%10 + 1 for x in row]
#                   for s in range(5) for row in riskLevels];

#     riskLevels = [[x+s if x+s <= 9 else (x+s)%10 + 1
#                     for s in range(5) for x in row] for row in riskLevels];

#     risk = calcRisks(riskLevels);

#     print("Part 2: {:d}".format(risk));

# # %% MAIN CALLS
# if __name__ == "__main__":

#     print("Solving Day 15, AoC 2021");

#     problem = read();
#     partOneOutput = partOne(problem)
#     partTwo(problem, partOneOutput);

#%% Other Solution
from heapq import heappush, heappop;

def read():

    with open("problem.txt") as problemFile:
        problem = [[int(x) for x in row.strip()]
                   for row in problemFile.readlines()];

    return problem;

def longFormDijkstra(riskLevels):

    def decode(value):
        risk = value % 10;
        F = (value % 1_000_000) // 10
        B = (value // 1_000_000);
        return risk, F, B;
    
    def encode(risk, F, B):
        return risk + 10*F + 1_000_000*B;

    def hasF(value):
        F = (value % 1_000_000) // 10
        return F != 0;

    def hasB(value):
        B = (value // 1_000_000);
        return B != 0;

    def hasFB(value):
        return hasF(value) and hasB(value);

    def getFB(value):
        risk, F, B = decode(value);
        return F + B;

    riskLevels = [[-1, *row, -1] for row in riskLevels]
    riskLevels = [[-1]*len(riskLevels[0]), *riskLevels, [-1]*len(riskLevels[0])];

    #riskLevels = [[[x, None, None] for x in row] for row in riskLevels];

    nR, nC = len(riskLevels), len(riskLevels[0]);

    start = (1, 1);
    end = (nR-2, nC-2);

    endRisk = riskLevels[-2][-2];
    
    riskLevels[1][1] = 0;
    riskLevels[-2][-2] = encode(endRisk, 0, endRisk);
    
    heapForward, heapBackward = [(0, start)], [(endRisk, end)];
    currentDistForward, currentForward = 0, start;
    currentDistBackward, currentBackward = endRisk, end;

    while heapForward or heapBackward:

        rF, cF = currentForward;
        rB, cB = currentBackward;

        for rp, cp in ((rF, cF+1), (rF+1, cF), (rF, cF-1), (rF-1, cF)):
            neighbor = (rp, cp);
            risk, F, B = decode(riskLevels[rp][cp]);
            if (risk > 0):
                dist = currentDistForward + risk;
                if (F == None or dist < F):
                    riskLevels[rp][cp] = encode(risk, dist, B);
                    heappush(heapForward, (dist, neighbor));

        for rp, cp in ((rB, cB+1), (rB+1, cB), (rB, cB-1), (rB-1, cB)):
            neighbor = (rp, cp);
            risk, F, B = decode(riskLevels[rp][cp]);
            if (risk > 0):
                dist = currentDistBackward + risk;
                if (B == None or dist < B):
                    riskLevels[rp][cp] = encode(risk, F, dist);
                    heappush(heapBackward, (dist, neighbor));

        if hasF(riskLevels[rB][cB]) or hasB(riskLevels[rB][cB]):
            
            w = min(((r, c) for r in range(nR) for c in range(nC) if hasFB(riskLevels[r][c])), 
                    key=lambda k: getFB(riskLevels[k[0]][k[1]]));
            print(w);
            return getFB(riskLevels[w[0]][w[1]]) - riskLevels[w[0]][w[1]][0];

        riskLevels[rF][cF] *= -1;
        riskLevels[rB][cB] *= -1;

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

    print("Part 2: {:d}".format(risk));

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day 15, AoC 2021");

    problem = read();
    partOne(problem);
    partTwo(problem);
