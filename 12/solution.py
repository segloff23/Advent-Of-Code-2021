
def read():

    with open("problem.txt") as problemFile:
        problem = {};
        for line in problemFile.readlines():
            a, b = line.strip().split("-");
            if a in problem:
                problem[a].append(b);
            else:
                problem[a] = [b];
            if b in problem:
                problem[b].append(a);
            else:
                problem[b] = [a];

    return problem;

def partOne(problem):

    def countPaths(visited, cameFrom, goal):

        if (cameFrom == goal):
            return 1;
        else:
            count = 0;
            for n in problem[cameFrom]:
                if n in bigs:
                    count += countPaths(visited, n, goal);
                elif n not in visited:
                    count += countPaths(visited.union({n}), n, goal);
            return count;

    start = "start";
    end = "end";

    bigs = set(loc for loc in problem if loc.isupper())

    count = countPaths({start}, start, end);

    print("Part 1: {:d}".format(count));

def partTwo(problem):

    def countPaths(visited, revisited, cameFrom, goal):

        if (cameFrom == goal):
            return 1;
        else:
            count = 0;
            for n in problem[cameFrom]:
                if n in bigs:
                    count += countPaths(visited, revisited, n, goal);
                elif n not in visited:
                    count += countPaths(visited.union({n}), revisited, n, goal);
                elif n != "start" and not revisited:
                    count += countPaths(visited.union({n}), True, n, goal);
            return count;

    bigs = set(loc for loc in problem if loc.isupper())

    start = "start";
    end = "end";

    count = countPaths({start}, False, start, end);

    print("Part 2: {:d}".format(count));

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day 12, AoC 2021");

    problem = read();

    partOne(problem);
    partTwo(problem);
