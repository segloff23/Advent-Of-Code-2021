class GeneralHeap(list):
    # Heap contains arbitrary objects
    #   isEqual(a, b) is used for searching the heap for a given object
    #   isLess(a, b) is used for structuring the heap

    def __init__(self, isEqual, isLess):
         super().__init__();
         self.isEqual = isEqual;
         self.isLess = isLess;

    def insert(self, node):
        self.append(node);
        self.upHeap(len(self)-1);

    def decreaseKey(self, node, updater):

        for k in range(len(self)):
            if (self.isEqual(node, self[k])):
                updater();
                self.upHeap(k);
                return;

        raise KeyError;

    def increaseKey(self, node, updater):

        for k in range(len(self)):
            if (self.isEqual(node, self[k])):
                updater();
                self.downHeap(k);
                return;

        raise KeyError;

    def extractMin(self):
        
        if (len(self) > 1):
            node = self[0];
            self[0] = self.pop();
            self.downHeap(0);
        else:
            node = self.pop();

        return node;

    def upHeap(self, child):

        parent = (child + 1) // 2 - 1;
        while (parent >= 0 and self.isLess(self[child], self[parent])):
            self[parent], self[child] = self[child], self[parent];
            child = parent;
            parent = (child + 1) // 2 - 1;

    def downHeap(self, parent):

        done = False;
        while (not done):

            left = 2*parent + 1;
            right = 2*parent + 2;
            swap = parent;

            if (left >= len(self)):
                done = True;
            else:
                if (self.isLess(self[left], self[swap])):
                    swap = left;
                if (right < len(self)) and (self.isLess(self[right], self[swap])):
                    swap = right;
                if (swap != parent):
                    self[swap], self[parent] = self[parent], self[swap];
                    parent = swap;
                else:
                    done = True;
class GeneralSolver:

    def __init__(self, graph, source, dest):

        self.graph = graph;
        self.source = source;
        self.dest = dest;

        self.reset();

    def reset(self):

        self.finalized = set();
        self.pi = {self.source: (None, 0)};

        self.heap = GeneralHeap(lambda a,b: a == b,
                                lambda a,b: self.pi[a][1] < self.pi[b][1]);
        self.heap.insert(self.source);

        self.last = None;
        self.current = self.source;
        self.isDone = False;

    def updatePi(self, node, value):
        self.pi[node] = value;

    def step(self):

        baseDist = self.pi[self.current][1];
        for neighbor in self.graph.getNeighbors(self.current):
            if neighbor not in self.finalized:
                dist = self.graph.getDistance(self.current, neighbor);
                if (dist != None):
                    if (neighbor not in self.pi):
                        self.pi[neighbor] = (self.current, dist + baseDist);
                        self.heap.insert(neighbor);
                    elif (dist + baseDist < self.pi[neighbor][1]):
                        self.heap.decreaseKey(neighbor, lambda : self.updatePi(neighbor, (self.current, dist)));

        if (self.current == self.dest):
            self.last = self.current;
            self.isDone = True;
        else:
            self.finalized.add(self.current);
            self.last = self.current;
            self.current = None;
            if (len(self.heap) != 0):
                smallest = self.heap.extractMin();
                if (self.pi[smallest][1] != None):
                    self.current = smallest;
            self.isDone = (self.current == None);

    def constructPath(self, end):

        path = [];
        current = end;
        while (self.pi[current][0] != None):
            path.append(current);
            current = self.pi[current][0];
        path.append(current);

        return list(reversed(path));

class Dijkstra:

    def solve(graph, source, dest):

        forward = GeneralSolver(graph, source, dest);
        backward = GeneralSolver(graph, dest, source);

        while (not (forward.isDone or backward.isDone)):

            forward.step();
            backward.step();

            if (forward.last == dest):

                dist = forward.pi[forward.last][1];
                route = forward.constructPath(dest)

                return (route, dist);

            elif (backward.last == source):

                dist = forward.pi[backward.last][1];
                route = list(reversed(backward.constructPath(source)));

                return (route, dist);

            elif (forward.last in backward.pi) or (backward.last in forward.pi):

                w = forward.last if (forward.last in backward.pi) else backward.last;
                dist = forward.pi[w][1] + backward.pi[w][1];

                for x in forward.pi:
                    if (x in backward.pi):
                        newDist = forward.pi[x][1] + backward.pi[x][1];
                        if (newDist < dist):
                            w = x;
                            dist = newDist;

                routeF = forward.constructPath(w);
                routeB = backward.constructPath(w);
                route = routeF[:-1] + list(reversed(routeB));

                return (route, dist);

        return ([], None);
