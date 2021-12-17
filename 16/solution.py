
def read():

    with open("problem.txt") as problemFile:
        problem = problemFile.read().strip();
    return problem;

def parsePacket(packet):

    def parseSubpackets(bitString, lengthID, length):

        subpackets = [];
        if lengthID == 0:
            j = 0;
            while j < length:
                sub, offset = parsePacket(bitString[j:]);
                subpackets.append(sub);
                j += offset;
        else:
            count = 0;
            j = 0;
            while count < length:
                sub, offset = parsePacket(bitString[j:]);
                subpackets.append(sub);
                j += offset;
                count += 1;

        return subpackets, j

    i = 0;
    version = int(packet[i:i+3], 2);
    i += 3;
    typeID = int(packet[i:i+3], 2);
    i += 3;
    if typeID == 4:
        bits = "";
        while packet[i] != "0":
            bits += packet[i+1:i+5];
            i += 5;
        bits += packet[i+1:i+5];
        i += 5;
        args = int(bits, 2);
    else:
        lengthID = int(packet[i], 2);
        i += 1;
        if lengthID == 0:
            length = int(packet[i:i+15], 2);
            i += 15;
        elif lengthID == 1:
            length = int(packet[i:i+11], 2);
            i += 11;

        args, offset = parseSubpackets(packet[i:], lengthID, length);
        i += offset;

    return (version, typeID, args), i;

def partOne(problem):

    def sumVersions(packet):

        version, typeID = packet[0:2];
        if typeID == 4:
            return version;
        else:
            subpackets = packet[2];
            return version + sum(sumVersions(p) for p in subpackets);

    bitString = "".join(bin(int(c, 16))[2:].zfill(4) for c in problem);

    packet, _ = parsePacket(bitString);

    total = sumVersions(packet)

    print("Part 1: {:d}".format(total));

    return packet;

def partTwo(problem, packet):

    def evaluate(packet):

        version, typeID, args = packet;

        if typeID == 0:
            value = sum(evaluate(p) for p in args);
        elif typeID == 1:
            value = 1;
            for p in args:
                value *= evaluate(p);
        elif typeID == 2:
            value = min(evaluate(p) for p in args)
        elif typeID == 3:
            value = max(evaluate(p) for p in args)
        elif typeID == 4:
            value = args;
        elif typeID == 5:
            left, right = args
            value = int(evaluate(left) > evaluate(right));
        elif typeID == 6:
            left, right = args
            value = int(evaluate(left) < evaluate(right));
        elif typeID == 7:
            left, right = args
            value = int(evaluate(left) == evaluate(right));
        else:
            raise Exception("Invalid type ID found");

        return value;

    value = evaluate(packet);

    print("Part 2: {:d}".format(value));

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day 16, AoC 2021");

    problem = read();
    partOneAnswer = partOne(problem);
    partTwo(problem, partOneAnswer);
