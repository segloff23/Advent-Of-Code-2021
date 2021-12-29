
def read():

    with open("problem.txt") as problemFile:
        pOneLine, pTwoLine = problemFile.readlines();
        pOne = int(pOneLine.split(" ")[-1]);
        pTwo = int(pTwoLine.split(" ")[-1]);

    return [pOne, pTwo];

def partOne(problem):

    pos = [*problem];
    scores = [0, 0];
    die = 1;
    player = 0;
    rollCount = 0;
    while (scores[1-player] < 1000):

        roll = 0;
        for k in range(3):
            roll += die;
            die = (die % 100) + 1;
        rollCount += 3;
        pos[player] = ((pos[player] + roll - 1) % 10) + 1;
        scores[player] += pos[player]
        player = 1 - player;

    answer = min(scores) * rollCount;

    print("Part 1: {:d}".format(answer));

    return 0;

def partTwo(problem, partOneOutput):

    cache = {};
    def DP(subprob):

        if (subprob not in cache):
            scores, pos, turn = subprob;
            if scores[0] >= 21:
                cache[subprob] = (1, 0);
            elif scores[1] >= 21:
                cache[subprob] = (0, 1);
            else:
                pOneWins, pTwoWins = 0, 0;
                for roll in rollFreq:

                    newPos = ((pos[turn] + roll - 1) % 10) + 1;
                    newScore = scores[turn] + newPos;

                    if (turn == 0):
                        newSubproblem = ((newScore, scores[1]), (newPos, pos[1]), 1);
                    else:
                        newSubproblem = ((scores[0], newScore), (pos[0], newPos), 0);

                    pOneInc, pTwoInc = DP(newSubproblem);
                    pOneWins += rollFreq[roll] * pOneInc;
                    pTwoWins += rollFreq[roll] * pTwoInc;

                cache[subprob] = (pOneWins, pTwoWins);

        return cache[subprob];

    rollFreq = {};
    for r1 in range(1, 4):
        for r2 in range(1, 4):
            for r3 in range(1, 4):
                total = r1 + r2 + r3;
                if total in rollFreq:
                    rollFreq[total] += 1;
                else:
                    rollFreq[total] = 1;

    pos = tuple(problem);
    answer = max(DP(((0, 0), pos, 0)));

    print("Part 2: {:d}".format(answer));

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day 21, AoC 2021");

    problem = read();
    partOneOutput = partOne(problem);
    partTwo(problem, partOneOutput);
