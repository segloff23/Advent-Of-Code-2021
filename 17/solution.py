
import re;

def read():

    with open("problem.txt") as problemFile:
        pattern = re.compile(r"target area: x=(\d+)..(\d+), y=(-?\d+)..(-?\d+)");
        m = re.match(pattern, problemFile.read());
        X = (int(m.group(1)), int(m.group(2)));
        Y = (int(m.group(3)), int(m.group(4)));
        problem = (X, Y);

    return problem;

def partOne(problem):

    X, Y = problem;
    
    # (v^2 + v) / 2 is the farthest it can go,
    # solve for X[0] to makesure it can reach
    vxMin = int((-1 + (1 + 8 * X[0]) ** 0.5) / 2);
    vxMax = X[1];
    
    vyMin = Y[0];
    vyMax = abs(Y[0]);
    
    passed = set();
    for vx0 in range(vxMin, vxMax+1):
        for vy0 in range(vyMin, vyMax+1):
            vx, vy = vx0, vy0;
            x, y = 0, 0;
            highest = 0;
            while y >= Y[0] and x <= X[1]:
                x += vx;
                y += vy;
                if vx > 0:
                    vx -= 1;
                vy -= 1;
                if (x >= X[0] and x <= X[1] and y >= Y[0] and y <= Y[1]):
                    passed.add((vx0, vy0));
                    break;
    
    highest = max(passed, key=lambda x: x[1])[1];
    
    height = (highest ** 2 + highest) // 2;
    numValid = len(passed);
    
    print("Part 1: {:d}".format(height));
    
    return numValid;

def partTwo(numValid, partOneOutput):

    numValid = partOneOutput;

    print("Part 2: {:d}".format(numValid));

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day 17, AoC 2021");

    problem = read();
    partOneOutput = partOne(problem);
    partTwo(problem, partOneOutput);
