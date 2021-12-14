
def read():

    with open("problem.txt") as problemFile:
        value, data = problemFile.read().strip().split("\n\n")
        start = value.strip();
        rules = {}
        for line in data.split("\n"):
            left, right = line.strip().split(" -> ");
            rules[left] = right;

    return (start, rules);

def polymerize(start, rules, steps):

    pairTransformation = {pair: [] for pair in rules};
    for n, pair in enumerate(rules):
        A = pair[0] + rules[pair];
        B = rules[pair] + pair[1];
        pairTransformation[pair].extend([A, B]);

    pairFreq = {pair: 0 for pair in rules};
    for i in range(len(start)-1):
        pairFreq[start[i:i+2]] += 1;

    letters = {c: start.count(c) for c in set(start)};
    for k in range(steps):
        newPairFreq = {pair: pairFreq[pair] for pair in pairFreq}
        for pair in pairFreq:
            change = pairFreq[pair];
            for newPair in pairTransformation[pair]:
                newPairFreq[newPair] += change;
            newPairFreq[pair] -= change;

            if rules[pair] not in letters:
                letters[rules[pair]] = change;
            else:
                letters[rules[pair]] += change;
        pairFreq = newPairFreq;

    return pairFreq, letters;

def partOne(problem):

    start, rules = problem;

    _, letters = polymerize(start, rules, 10);

    keyLookup = lambda k: letters[k];

    best = max(letters, key=keyLookup);
    worst = min(letters, key=keyLookup);

    diff = letters[best] - letters[worst];

    print("Part 1: {:d}".format(diff));

def partTwo(problem):

    start, rules = problem;

    _, letters = polymerize(start, rules, 40);

    keyLookup = lambda k: letters[k];

    best = max(letters, key=keyLookup);
    worst = min(letters, key=keyLookup);

    diff = letters[best] - letters[worst];

    print("Part 2: {:d}".format(diff));

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day 14, AoC 2021");

    problem = read();

    partOne(problem);
    partTwo(problem);
