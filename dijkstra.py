# Libraries
import time
import sys
import heapq
import tracemalloc

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

def backtrack(parent, start, target):                                       # takes the parent list from our Dijkstra Algorithm and reconstructs the path it took to get from the starting node and to a target
    path = []                                                               # init array holding our path
    current = target                                                        # our current node is the target

    while current != -1:                                                    # walk from our current node till we reach the starting node
        path.append(current)                                                # add to our path the current node we are on
        current = parent[current]                                           # the parent array holds the previous node hop for each node, we hop to the previous node, making it our current node
    path.reverse()                                                          # when done reverse the order
    if path[0] == start:                                                    # if done right, our first element should equal to our starting node
        return path
    return []                                                               # if not we didn't find a path

def arrayBasedDijkstra(g, start):                                           # array-based Dijkstra's Algorithm, usage: output, parent = arrayBasedDijkstra((class)graph, (int)startNode)
    print(f"Start array Dijkstra at node {start} | ", end="")                                      
    dist = [sys.maxsize] * g.v                                              # initialize our distance array with total elements equal to vertex count of graph, setting all distances to infinity
    visited = [False] * g.v                                                 # initialize our visited array with total elements equal to vertex count of grpah, setting all visited nodes to false
    dist[start] = 0                                                         # initialize our starting node distance to 0

    parent = [-1] * g.v                                                     # initialize our parent array with total elements equal to vertex, setting all elements to -1. this array will hold the previous node hop for each node.

    if(not g.sparse):                                                       # if the graph is dense, we will use the adjacency matrix representation of the graph
        print("isDense -> using adjList| ", end="")
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
                        parent[neighbor] = node                             # update our parent array for our neighbor, saying we got here from this node
    else:                                                                   # else if the graph is a sparse graph, we will use the adjacency list representation of the graph, same logic as above!
        print("isSparse -> using adjMatrix | ", end="")                      
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
                        parent[neighbor] = node
    print(f"{dist} | parent: ", end="")
    print(parent)
    return dist, parent

def priorityQueueBasedDijkstra(g, start):                                   # priority queue based Dijkstra's Algorithm, usage: output, parent = priorityQueueBasedDijkstra((class)graph, (int)startNode)
    print(f"Start prio.q Dijkstra at node {start} | ", end="")
    priorityQueue = []                                                      # init priority queue
    dist = [sys.maxsize] * g.v                                              # init our dist array (see arrayBasedDijkstra for more info)
    dist[start] = 0                                                         # init our starting node in dist array
    heapq.heappush(priorityQueue, (0, start))                               # push the weight and start node to heap

    parent = [-1] * g.v                                                     # init parent array

    while priorityQueue:                                                    # while there are still items in the priority queue
        minWeight, node = heapq.heappop(priorityQueue)                      # pop the last accessed node and its weight

        if minWeight > dist[node]:                                          # if that weight is greater than the current distance known distance to the node skip
            continue

        for neighbor, weight in g.list[node]:                               # look for the neighbor nodes and its weights next to our node
            if dist[node] + weight < dist[neighbor]:                        # if the weight to neighbor nodes + distance to get to current node is less than our known shortest path update the node
                dist[neighbor] = dist[node] + weight;                       # update the shortest distance
                parent[neighbor] = node                                     # add to our parent list
                heapq.heappush(priorityQueue, (dist[neighbor], neighbor))   # push to heap
    print(f"{dist} | parent: ", end="")
    print(parent)
    return dist, parent

def run_experiment(g, source, target, trials=5):                            # takes a graph, start node, target node, and tests it using both Dijkstra's Algorithm a number of trial times, usage: run_experiment((graph)g, (int)start_node, (int)target)
    print(f"\nRunning benchmarks for {g.name} (V={g.v}, E={g.edges})")

    total_time_array = 0                                                    # init variables to hold total time and mem usage
    peak_memory_array = 0
    for i in range(trials):                                                 # test 5 times
        print(f"#{i} | ", end="")
        tracemalloc.start()                                                 # start malloc and time counters
        start_time = time.perf_counter()

        dist_array, path = arrayBasedDijkstra(g, source)                    # run algo

        end_time = time.perf_counter()                                      # end our counters
        _ , peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        total_time_array += (end_time - start_time)                         # add the duration to total time and mem
        peak_memory_array = max(peak_memory_array, peak)
        print(f"    Target: {target} | Path reconstruction: {backtrack(path, source, target)}")

    avg_time_array = (total_time_array / trials) * 1000                     # calculate the avg time and mem
    mem_array_mb = peak_memory_array / (1024 * 1024)

    total_time_heap = 0                                                     # do the same for priority based Dijkstra
    peak_memory_heap = 0
    for i in range(trials):
        print(f"#{i} | ", end="")
        tracemalloc.start()
        start_time = time.perf_counter()

        dist_heap, path = priorityQueueBasedDijkstra(g, source)

        end_time = time.perf_counter()
        _ , peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        total_time_heap += (end_time - start_time)
        peak_memory_heap = max(peak_memory_heap, peak)
        print(f"    Target: {target} | Path reconstruction: {backtrack(path, source, target)}")

    avg_time_heap = (total_time_heap / trials) * 1000
    mem_heap_mb = peak_memory_heap / (1024 * 1024)

    # Output Results for Table
    representation = "Matrix" if not g.sparse else "List"
    print(f"  Array ({representation}): {avg_time_array:.4f} ms | {mem_array_mb:.6f} MB")
    print(f"  Heap (List):     {avg_time_heap:.4f} ms | {mem_heap_mb:.6f} MB")
    print(f"  Distances Match: {dist_array == dist_heap}")       

def main(): 
    spars1, spars2, dens1, dens2, dens3 = initGraphs()

    spars1.printGraph()
    spars2.printGraph()
    dens1.printGraph()
    dens2.printGraph()
    dens3.printGraph()

    run_experiment(spars1, 0, 5)
    run_experiment(spars2, 0, 6)
    run_experiment(dens1, 0, 4)
    run_experiment(dens2, 0, 5)
    run_experiment(dens3, 3, 0)
if __name__ == "__main__":
    main()