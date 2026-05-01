# Libraries
import time
import sys
import numpy as np

# Constants ----------------------------------------

# ---------------------------------------------------

class graph:                                                                # class graph, usage: variableName = graph((string)"name of graph", (int)totalNodes) 
    def __init__(self, varName, nodeCount):
        self.name = varName                                                 # (string) name of the graph, usage: name_of_graph = variableName.name
        self.v = nodeCount                                                  # (int) number of nodes/vertices in graph, usage: totalNodes = variableName.v
        self.edges = 0                                                      # (int) number of edges in graph, usage: totalEdges = variableName.edges
        self.sparse = True                                                  # (bool) self.sparse == True is a sparse graph, not self.sparse == True  is a dense graph
        self.list = [[] for _ in range(self.v)]                             # init a list/matrix for each graph
        self.matrix = [[-1 for _ in range(self.v)] for _ in range(self.v)]

    def addEdge(self, node, dest, weight):                                  # adds an edge to an undirected graph, usage: addEdge((int)sourceNode, (int)destinationNode, (int)weight)
        self.list[node].append((dest, weight))
        self.list[dest].append((node, weight))

        self.matrix[node][dest] = weight
        self.matrix[dest][node] = weight

        self.edges += 1
        if self.edges > (0.5 * self.v * (self.v - 1)) / 2:                  # checks for sparseness or denseness
            self.sparse = False

    def printGraph(self):                                                   # prints the graph out in style adjacency list or matrix, usage: variableName.printGraph()
        print(f"{self.name}\n{self.v} vertices\n{self.edges} edges\nIs sparse?: {self.sparse}\nIs dense?: {not self.sparse}\nAdj List")
        for i in range(self.v):
            print(self.list[i])
        print(f"Adj Matrix")
        for row in self.matrix:
            print(row)
        print()

def initGraphs():                                                           # initializes 5 graphs
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

    dens3 = graph("dens3", 8)   # custom graph
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

def arrayBasedDijkstra(g, start):                                           # array-based Dijkstra's Algorithm, usage: output = arrayBasedDijkstra((class)graph, (int)startNode)
    print("Starting array-based Dijkstra Algorithm")                                      
    dist = [sys.maxsize] * g.v                                              # initialize our distance array with total elements equal to vertex count of graph, setting all distances to infinity
    visited = [False] * g.v                                                 # initialize our visited array witwh total elements equal to vewrtex count of grpah, setting all visited nodes to false
    dist[start] = 0                                                         # initialize our starting node distance to 0

    if(not g.sparse):                                                       # if the graph is dense, we will use the adjacency matrix representation of the graph
        print("Graph is dense: Using adjacency matrix")
        for _ in range(g.v):                                                # loop through the total number of vertices
            node = -1                                                       # initialize variable which will hold the node with least cost
            minWeight = sys.maxsize                                         # initialize variable which will hold the least cost edge
            for i in range(g.v):                                            # loop through each vertices. if a vertex hasn't been visited and their edge cost is the smallest out of the unvisited, we will visit that node
                if not visited[i] and dist[i] < minWeight:
                    minWeight = dist[i]
                    node = i
            if node == -1: break                                            # if we don't find a visited node, we are done
            visited[node] = True                                        

            for neighbor in range(g.v):                                     # look through the row of our node, checking all vertices to see if they have an edge
                if g.matrix[node][neighbor] > 0 and not visited[neighbor]:  # if our visited node has an edge with another node, the weight is > 0, and if it is not visited, we enter our relaxation rule
                    if dist[node] + g.matrix[node][neighbor] < dist[neighbor]:  # if the new total distance from current node to neighboring node is less than the existing known route to the neighboring node, we relax the known shortest distance
                        dist[neighbor] = dist[node] + g.matrix[node][neighbor]; # we set the new route with shortest distance as the new known shortest path
    else:                                                                   # else if the graph is a sparse graph, we will use the adjacency list representation of the graph, same logic as above!
        print("Graph is sparse: Using adjacency list")                      
        for _ in range(g.v):
            node = -1
            minWeight = sys.maxsize
            for i in range(g.v):
                if not visited[i] and dist[i] < minWeight:
                    minWeight = dist[i]
                    node = i
            if node == -1: break
            visited[node] = True

            for neighbor, weight in g.list[node]:
                if weight > 0 and not visited[neighbor]:
                    if dist[node] + weight < dist[neighbor]:
                        dist[neighbor] = dist[node] + weight;
           
    return dist

def priorityQueueBasedDijkstra(g, start):
    print("placehodler")
        

def main(): 
    spars1, spars2, dens1, dens2, dens3 = initGraphs()

    spars1.printGraph()
    spars2.printGraph()
    dens1.printGraph()
    dens2.printGraph()
    dens3.printGraph()

    print(arrayBasedDijkstra(spars1, 0))

if __name__ == "__main__":
    main()