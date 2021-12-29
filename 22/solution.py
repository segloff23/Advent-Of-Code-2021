
import re;

def read():

    with open("problem.txt") as problemFile:
        pattern = re.compile(r"(on|off) x=([-\d]+)..([-\d]+),y=([-\d]+)..([-\d]+),z=([-\d]+)..([-\d]+)");
        problem = [];
        for line in problemFile.readlines():
            m = re.match(pattern, line);
            state = m.group(1);
            X = (int(m.group(2)), int(m.group(3)));
            Y = (int(m.group(4)), int(m.group(5)));
            Z = (int(m.group(6)), int(m.group(7)));
            problem.append((state, (X, Y, Z)));

    return problem;

def doesIntersect(cube, cubesToCheck):
    
    for otherCube in cubesToCheck:
        intersects = True;
        for A, B in zip(cube, otherCube):
            if not ((A[0] <= B[0] and B[0] <= A[1]) or (B[0] <= A[0] and A[0] <= B[1])):
                intersects = False;
                break;
        if (intersects):
            return True;

    return False;

def updateCubeList(cube, cubesToUpdate, toggle):

    X_A, Y_A, Z_A = cube;
    
    newCubes = [];
    for otherCube in cubesToUpdate:
        if doesIntersect(cube, [otherCube]):

            X_B, Y_B, Z_B = otherCube;
            if (X_B[0] <= X_A[0] and X_A[0] <= X_B[1]):
                if X_B[0] <= X_A[0]-1:
                    newCubes.append(((X_B[0], X_A[0]-1), Y_B, Z_B));
                    X_B = (X_A[0], X_B[1]);
            if (X_B[0] <= X_A[1] and X_A[1] <= X_B[1]):
                if X_B[1] >= X_A[1]+1:
                    newCubes.append(((X_A[1]+1, X_B[1]), Y_B, Z_B));
                    X_B = (X_B[0], X_A[1]);
            
            if (Y_B[0] <= Y_A[0] and Y_A[0] <= Y_B[1]):
                if Y_B[0] <= Y_A[0]-1:
                    newCubes.append((X_B, (Y_B[0], Y_A[0]-1), Z_B));
                    Y_B = (Y_A[0], Y_B[1]);
            if (Y_B[0] <= Y_A[1] and Y_A[1] <= Y_B[1]):
                if Y_B[1] >= Y_A[1]+1:
                    newCubes.append((X_B, (Y_A[1]+1, Y_B[1]), Z_B));
                    Y_B = (Y_B[0], Y_A[1]);
            
            if (Z_B[0] <= Z_A[0] and Z_A[0] <= Z_B[1]):
                if Z_B[0] <= Z_A[0]-1:
                    newCubes.append((X_B, Y_B, (Z_B[0], Z_A[0]-1)));
                    Z_B = (Z_A[0], Z_B[1]);
            if (Z_B[0] <= Z_A[1] and Z_A[1] <= Z_B[1]):
                if Z_B[1] >= Z_A[1]+1:
                    newCubes.append((X_B, Y_B, (Z_A[1]+1, Z_B[1])));
                    Z_B = (Z_B[0], Z_A[1]);
        else:
            newCubes.append(otherCube);

    if toggle == "on":
        newCubes.append(cube);

    return newCubes;

def calcVolume(onCubes):

    volume = 0;
    for X, Y, Z in onCubes:
        volume += (X[1]-X[0]+1)*(Y[1]-Y[0]+1)*(Z[1]-Z[0]+1);

    return volume;

def toggleCubes(instructions):

    onCubes = [];
    for toggle, cube in instructions:
        onCubes = updateCubeList(cube, onCubes, toggle);

    return onCubes;

def partOne(problem):

    onCubes = toggleCubes(problem);
    
    trimmedOnCubes = [];
    for X, Y, Z in onCubes:

        if X[0] < -50:
            X = (-50, X[1]);
        elif X[0] > 50:
            continue;

        if X[1] > 50:
            X = (X[0], X[1]);
        elif X[1] < -50:
            continue;

        if Y[0] < -50:
            Y = (-50, Y[1]);
        elif Y[0] > 50:
            continue;

        if Y[1] > 50:
            Y = (Y[0], Y[1]);
        elif Y[1] < -50:
            continue;

        if Z[0] < -50:
            Z = (-50, Z[1]);
        elif Z[0] > 50:
            continue;

        if Z[1] > 50:
            Z = (Z[0], Z[1]);
        elif Z[1] < -50:
            continue;
        
        trimmedOnCubes.append((X, Y, Z));
    
    volume = calcVolume(trimmedOnCubes);   

    print("Part 1: {:d}".format(volume));

    return onCubes;

def partTwo(problem, partOneOutput):

    volume = calcVolume(partOneOutput);
    
    print("Part 2: {:d}".format(volume));

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day 22, AoC 2021");

    problem = read();
    partOneOutput = partOne(problem);
    partTwo(problem, partOneOutput);
