
def read():

    with open("problem.txt") as problemFile:
        problem = [];
        for line in problemFile.readlines():
            ins = [x.strip() for x in line.split(" ")];
            if (len(ins) == 3 and ins[-1] not in "wxyz"):
                ins[-1] = int(ins[-1]);
            problem.append(ins);

    return problem;

def parseBlocks(instructions):

    blocks = [];
    n = 0;
    while (n < len(instructions)):
        block = [];
        n += 1;
        while (n < len(instructions) and instructions[n][0] != "inp"):
            block.append(instructions[n]);
            n += 1;
        blocks.append(block);

    return blocks;

def run(blocks, W):

    z = [];
    for n, (D, R, Q) in enumerate(blocks):
        w = W[n];
        if D == 1: #push
            z.append(w + Q)
        else:
            x = z.pop();
            if (x + R != w):
                z.append(w + Q);

    total = sum(z[-p-1] * (26**p) for p in range(len(z)));

    return total;

def partOne(problem):

    blocks = parseBlocks(problem);

    cleanBlocks = [];
    for block in blocks:
        D = block[3][-1]; # 1 = push, 26 = pop
        R = block[4][-1]; # pop arg
        Q = block[14][-1]; # push arg
        cleanBlocks.append((D, R, Q));

    W = [0]*14;
    z = [];
    for n, (D, R, Q) in enumerate(cleanBlocks):
        if D == 1:
            z.append((Q, n))
        else:
            Q, n_q = z.pop();
            found = False;
            for w_n_q in range(9, 0, -1):
                for w_n_r in range(9, 0, -1):
                    if w_n_q + Q + R == w_n_r:
                        found = True;
                        break;
                if (found):
                    break;
            W[n_q] = w_n_q;
            W[n] = w_n_r;

    answer = "".join(str(x) for x in W);

    print("Part 1: {:s}".format(answer));

    return cleanBlocks;

def partTwo(problem, partOneOutput):

    cleanBlocks = partOneOutput;

    W = [0]*14;
    z = [];
    for n, (D, R, Q) in enumerate(cleanBlocks):
        if D == 1:
            z.append((Q, n))
        else:
            Q, n_q = z.pop();
            found = False;
            for w_n_q in range(1, 10):
                for w_n_r in range(1, 10):
                    if w_n_q + Q + R == w_n_r:
                        found = True;
                        break;
                if (found):
                    break;
            W[n_q] = w_n_q;
            W[n] = w_n_r;

    answer = "".join(str(x) for x in W);

    print("Part 2: {:s}".format(answer));

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day 24, AoC 2021");

    problem = read();
    partOneOutput = partOne(problem);
    partTwo(problem, partOneOutput);
