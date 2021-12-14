
def readWordList():

    with open("problem.txt") as problemFile:
        wordList = [w.strip() for w in problemFile.readlines()];

    return wordList;

def partOne(problem):

    B = len(problem[0]);
    N = len(problem);
    N2 = N // 2;

    counts = [[num[b] for num in problem].count("1") for b in range(B)];

    gammaBin = "".join(["1" if c > N2 else "0" for c in counts]);
    epsBin = "".join(["0" if c > N2 else "1" for c in counts]);

    product = int(gammaBin, 2) * int(epsBin, 2);

    print("Part 1: {:d}".format(product));

def partTwo(problem):

    def calcRating(numbers, keepFunc):

        B = len(numbers[0]);
        rating = [*numbers];

        bit = 0;
        while len(rating) > 1 and bit < B:

            oneCount = [num[bit] for num in rating].count("1")
            zeroCount = len(rating) - oneCount;

            keepBit = keepFunc(oneCount, zeroCount);
            rating = [num for num in rating if num[bit] == keepBit];
            bit += 1;

        if (len(rating) > 1):
            raise Exception;

        return rating[0];

    O2keep = lambda ones, zeroes: "1" if ones >= zeroes else "0";
    O2rating = calcRating(problem, O2keep);

    CO2keep = lambda ones, zeroes: "1" if ones < zeroes else "0";
    CO2rating = calcRating(problem, CO2keep);

    product = int("".join(O2rating), 2) * int("".join(CO2rating), 2);

    print("Part 2: {:d}".format(product));

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day 03, AoC 2021");

    problem = readWordList();

    partOne(problem);
    partTwo(problem);
