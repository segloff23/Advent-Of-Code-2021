
def read():

    with open("problem.txt") as problemFile:
        problem = [];
        for line in problemFile.readlines():
            problem.append(eval(line));

    return problem;

class Node:

    def __init__(self, children, parent=None):

        if (parent != None):
            self.depth = parent.depth + 1;
        else:
            self.depth = 0;
        self.parent = parent;
    
        if isinstance(children, int):
            self.left = None;
            self.right = None;
            self.value = children;
        else:
            if (len(children) == 2):
                self.left = Node(children[0], parent=self);
                self.right = Node(children[1], parent=self);
            self.value = None;

    def __str__(self):
        if self.value != None:
            return str(self.value);
        else:
            return "[" + ", ".join([str(self.left), str(self.right)]) + "]"

def findFirstInt(node):

    left, right = node.left, node.right;
    if left.value != None:
        return left;

    first = findFirstInt(left);
    if (first != None):
        return first;

    if right.value != None:
        return right;

    first = findFirstInt(right);
    if (first != None):
        return first;

    return None;

def findLastInt(node):

    left, right = node.left, node.right;
    if right.value != None:
        return right;

    first = findLastInt(right);
    if (first != None):
        return first;
    
    if left.value != None:
        return left;

    first = findLastInt(left);
    if (first != None):
        return first;

    return None;

def findRightInt(node):

    parent = node.parent;
    if (parent == None):
        return None;

    if (node == parent.right):
        return findRightInt(node.parent);
    else:
        neighbor = parent.right;
        if (neighbor.value != None):
            return neighbor;
        else:
            return findFirstInt(neighbor);

def findLeftInt(node):

    parent = node.parent;
    if (parent == None):
        return None;

    if (node == parent.left):
        return findLeftInt(node.parent);
    else:
        neighbor = parent.left;
        if (neighbor.value != None):
            return neighbor;
        else:
            return findLastInt(neighbor);

def explode(node):

    if (node.value != None):
        return False;

    if (node.depth == 4):
        left, right = node.left, node.right;
        leftmost = findLeftInt(node);
        if (leftmost != None):
            leftmost.value += left.value;
        rightmost = findRightInt(node);
        if (rightmost != None):
            rightmost.value += right.value;
        node.left, node.right = None, None;
        node.value = 0;
        return True;
    else:
        didExplode = explode(node.left);
        didExplode = explode(node.right) or didExplode;
        return didExplode;
    return False;

def split(node):

    num = node.value;
    if (num != None and num >= 10):
        left = num // 2;
        right = left + (num % 2);
        node.left, node.right = Node(left, node), Node(right, node);
        node.value = None;
        return True;

    if (node.value == None):
        if split(node.left):
            return True;
        if split(node.right):
            return True;

    return False;

def updateDepths(node):
    
    parent = node.parent;
    if (parent != None):
        node.depth = parent.depth + 1;
    else:
        node.depth = 0;
    
    if (node.value == None):
        updateDepths(node.left);
        updateDepths(node.right);
    

def add(nodeA, nodeB):    

    parent = Node([]);
    parent.left, parent.right = nodeA, nodeB;
    nodeA.parent, nodeB.parent = parent, parent;
    updateDepths(parent);
    process(parent);

    return parent;

def process(snailfish):

    exploded, splitted = True, True;
    while (exploded or splitted):
        exploded = explode(snailfish);
        splitted = split(snailfish);

    return snailfish;

def magnitude(node):

    if (node.value != None):
        return node.value;

    return (3 * magnitude(node.left)) + (2 * magnitude(node.right));

def partOne(problem):

    nodeA, nodeB = Node(problem[0]), Node(problem[1]);

    snailfish = add(nodeA, nodeB);
    for B in problem[2:]:
        nodeB = Node(B);
        snailfish = add(snailfish, nodeB);

    M = magnitude(snailfish);

    print("Part 1: {:d}".format(M));

    return 0;

def partTwo(problem, partOneOutput):

    N = len(problem);

    best = 0;

    for i in range(N):
        for j in range(i+1, N):
            nodeA, nodeB = Node(problem[i]), Node(problem[j]);
            snailfish = add(nodeA, nodeB);
            M = magnitude(snailfish);
            if (M > best):
                best = M;

            nodeA, nodeB = Node(problem[j]), Node(problem[i]);
            snailfish = add(nodeA, nodeB);
            M = magnitude(snailfish);
            if (M > best):
                best = M;

    print("Part 2: {:d}".format(best));

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day 18, AoC 2021");

    problem = read();
    partOneOutput = partOne(problem);
    partTwo(problem, partOneOutput);
