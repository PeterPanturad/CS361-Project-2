# Libraries
import time
import numpy as np

# Constants ----------------------------------------

# ---------------------------------------------------

class graph:
    def __init__(self, varName, nodeCount):
        self.name = varName
        self.v = nodeCount
        self.edges = 0
        self.list = [[] for _ in range(self.v)]
        self.matrix = [[-1 for _ in range(self.v)] for _ in range(self.v)]

    def addEdge(self, node, dest, weight):
        self.list[node].append((dest, weight))
        self.list[dest].append((node, weight))

        self.matrix[node][dest] = weight
        self.matrix[dest][node] = weight

        self.edges += 1

    def printGraph(self):
        print(f"{self.name}\n{self.v} vertices\n{self.edges} edges\nAdj List")
        for i in range(self.v):
            print(self.list[i])
        print(f"Adj Matrix")
        for row in self.matrix:
            print(row)
        print()

def initGraphs():
    spars1 = graph("spars1", 6)
    spars1.addEdge(1, 0, 4)
    spars1.addEdge(1, 3, 5)
    spars1.addEdge(2, 0, 2)
    spars1.addEdge(2, 3, 1)
    spars1.addEdge(4, 3, 3)
    spars1.addEdge(4, 5, 2)

    spars2 = graph("spars2", 7)
    spars2.addEdge(1, 0, 3)
    spars2.addEdge(1, 3, 2)
    spars2.addEdge(1, 4, 5)
    spars2.addEdge(4, 2, 4)
    spars2.addEdge(4, 6, 1)
    spars2.addEdge(2, 0, 6)
    spars2.addEdge(3, 5, 7)

    dens1 = graph("dens1", 5)
    dens1.addEdge(0, 1, 2)
    dens1.addEdge(0, 2, 5)
    dens1.addEdge(0, 3, 1)
    dens1.addEdge(0, 4, 4)
    dens1.addEdge(1, 2, 3)
    dens1.addEdge(1, 3, 2)
    dens1.addEdge(1, 4, 6)
    dens1.addEdge(2, 3, 3)
    dens1.addEdge(2, 4, 1)
    dens1.addEdge(3, 4, 2)

    dens2 = graph("dens2", 6)
    dens2.addEdge(0, 1, 3)
    dens2.addEdge(0, 4, 5)
    dens2.addEdge(1, 2, 1)
    dens2.addEdge(2, 3, 3)
    dens2.addEdge(3, 4, 2)
    dens2.addEdge(4, 5, 1)
    dens2.addEdge(0, 2, 2)
    dens2.addEdge(1, 3, 2)
    dens2.addEdge(1, 4, 4)
    dens2.addEdge(2, 4, 6)
    dens2.addEdge(0, 3, 6)
    dens2.addEdge(0, 5, 4)
    dens2.addEdge(1, 5, 7)
    dens2.addEdge(2, 5, 5)
    dens2.addEdge(3, 5, 4)

    dens3 = graph("dens3", 8)
    dens3.addEdge(0, 1, 2)
    dens3.addEdge(0, 2, 5)
    dens3.addEdge(0, 4, 16)
    dens3.addEdge(0, 5, 9)
    dens3.addEdge(0, 6, 4)
    dens3.addEdge(0, 7, 5)
    dens3.addEdge(1, 2, 10)
    dens3.addEdge(1, 4, 4)
    dens3.addEdge(1, 6, 4)
    dens3.addEdge(1, 7, 6)
    dens3.addEdge(3, 2, 10)
    dens3.addEdge(3, 4, 4)
    dens3.addEdge(4, 2, 15)
    dens3.addEdge(4, 7, 10)
    dens3.addEdge(6, 5, 18)
    dens3.addEdge(6, 7, 2)

    return spars1, spars2, dens1, dens2, dens3

def main(): 
    spars1, spars2, dens1, dens2, dens3 = initGraphs()

    spars1.printGraph()
    spars2.printGraph()
    dens1.printGraph()
    dens2.printGraph()
    dens3.printGraph()

if __name__ == "__main__":
    main()