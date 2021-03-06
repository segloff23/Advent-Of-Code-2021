
def readWordList():

    with open("problem.txt") as problemFile:
        wordList = [w.strip() for w in problemFile.readlines()];

    return wordList;

def partOne(problem):

    R = len(problem);
    C = len(problem[0]);

    basins = [];
    risk = 0;
    for r in range(R):
        for c in range(C):
            isLowest = True;
            val = int(problem[r][c]);
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if (r+dr < R and c+dc < C and r+dr >= 0 and c+dc >= 0):
                    if int(problem[r+dr][c+dc]) <= val:
                        isLowest = False;
                        break;
            if isLowest:
                risk += 1 + val;
                basins.append((r, c));

    print("Part 1: {:d}".format(risk));

    return basins;

def partTwo(problem):

    def exploreNode(r, c, visited):
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if (r+dr < R and c+dc < C and r+dr >= 0 and c+dc >= 0):
                if (r+dr, c+dc) not in visited and problem[r+dr][c+dc] != "9":
                    visited.add((r+dr, c+dc));
                    exploreNode(r+dr, c+dc, visited);

    R = len(problem);
    C = len(problem[0]);

    visited = set();

    sizes = [];
    for r in range(R):
        for c in range(C):
            oldSize = len(visited);
            if problem[r][c] != "9" and (r, c) not in visited:
                visited.add((r, c));
                exploreNode(r, c, visited);
                newSize = len(visited);
                sizes.append(newSize - oldSize);

    sizes.sort(reverse=True);
    product = sizes[0] * sizes[1] * sizes[2];

    print("Part 2: {:d}".format(product));

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day 09, AoC 2021");

    problem = readWordList();

    partOne(problem);
    partTwo(problem);













