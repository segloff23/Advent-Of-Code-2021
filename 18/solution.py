# %% IMPORTS
# import re;
# import math;

# import numpy as np;
# import matplotlib.pyplot as plt;

# from collections import deque;
# from itertools import permutations;

def read():

    with open("problem.txt") as problemFile:
        problem = [];
        for line in problemFile.readlines():
            problem.append(eval(line));

    return problem;

class Node:

    def __init__(self, children, parent=None):

        if isinstance(children, int):
            self.children = None;
            self.value = children;
        else:
            self.children = [Node(child, parent=self) for child in children];
            self.value = None;

        self.parent = parent;

    def __str__(self):
        if self.value != None:
            return str(self.value);
        else:
            return "[" + ", ".join(str(child) for child in self.children) + "]"

    def getIndex(self):
        return self.parent.children.index(self);

def findFirstInt(node):

    if (node.children == None):
        return None;

    for child in node.children:
        if child.value != None:
            return child;
        value = findFirstInt(child);
        if (value != None):
            return value;

    return None;

def findLastInt(node):

    if (node.children == None):
        print("ere");
        return None;

    for child in reversed(node.children):
        if child.value != None:
            return child;
        value = findLastInt(child);
        if (value != None):
            return value;

    return None;

def findRightInt(node):

    parent = node.parent;
    if (parent == None):
        return None;

    index = node.getIndex();
    if (index == len(parent.children) - 1):
        return findRightInt(node.parent);
    else:
        neighbor = parent.children[index+1];
        if (neighbor.value != None):
            return neighbor;
        else:
            return findFirstInt(neighbor);

def findLeftInt(node):

    parent = node.parent;
    if (parent == None):
        return None;

    index = node.getIndex();
    if (index == 0):
        return findLeftInt(node.parent);
    else:
        neighbor = parent.children[index-1];
        if (neighbor.value != None):
            return neighbor;
        else:
            return findLastInt(neighbor);

def explode(node):

    if (node.value != None):
        return False;

    parentCount = 0;
    parent = node.parent;
    while (parent != None):
        parentCount += 1;
        parent = parent.parent;

    if (parentCount == 4):
        left, right = node.children;
        leftmost = findLeftInt(node);
        if (leftmost != None):
            leftmost.value += left.value;
        rightmost = findRightInt(node);
        if (rightmost != None):
            rightmost.value += right.value;
        node.children = None;
        node.value = 0;
        return True;
    else:
        for child in node.children:
            if explode(child):
                return True;

    return False;

def split(node):

    num = node.value;
    if (num != None and num >= 10):
        left = num // 2;
        right = left + (num % 2);
        node.children = [Node(left, node), Node(right, node)];
        node.value = None;
        return True;

    if (node.children != None):
        for child in node.children:
            if split(child):
                return True;

    return False;

def add(nodeA, nodeB):

    parent = Node([]);
    parent.children = [nodeA, nodeB];
    nodeA.parent, nodeB.parent = parent, parent;
    process(parent);

    return parent;

def process(snailfish):

    exploded, splitted = True, True;
    while (exploded or splitted):
        exploded, splitted = False, False;
        exploded = explode(snailfish);
        if (not exploded):
            splitted = split(snailfish);

    return snailfish;

def magnitude(node):

    if (node.value != None):
        return node.value;

    return (3 * magnitude(node.children[0])) + (2 * magnitude(node.children[1]));

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
    #partTwo(problem, partOneOutput);
