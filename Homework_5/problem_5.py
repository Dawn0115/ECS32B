# HW5 P5
# Please don't change any function names
# Vertex definition provided, please don't modify any of the provided code
# Add any helper methods if necessary
'''Author: YANGCHENG
Date: 3/16
description: implementation of BFS in graph.'''

class Vertex:
    def __init__(self, label):
        self.label = label
        self.neighbors = []
    def __str__(self):
        return self.label
    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)
        self.neighbors.sort()
# Graph definition provided, please don't modify any of the provided code
# Add any helper methods if necessary
class Graph:
    def __init__(self):
        self.vertices = []
# Add a vertex object
    def add_vertex(self, vertex):
        self.vertices.append(vertex)
# Get index of a vertex with corresponding label
# Return -1 if not found
    def get_vertex_index(self, label):
        index = 0
        for vertex in self.vertices:
            if label == str(vertex):
                return index
            index += 1
        return -1
# Find a vertex with corresponding label and return as Vertex object
    def find_vertex(self, label):
        for vertex in self.vertices:
            if label == str(vertex):
                return vertex
        return None
# Add an edge from a vertex with from_label to a vertex with to_label
# These vertices must already exist in the graph
    def add_edge(self, from_label, to_label):
        source_vertex = self.find_vertex(from_label)
        dest_vertex = self.find_vertex(to_label)
        if source_vertex is not None and dest_vertex is not None:
            source_vertex.add_neighbor(to_label)
# Perform breadth-first search on a directed graph g starting at vertex with label start_label
# Return a list of vertices' name in the order in which they are visited
# Remove the "pass" statement and implement the function

#implementing breadthFirst traversal
def breadthFirst(g, start_label):
    # define the starting vertex
    Start = g.find_vertex(start_label)
    #create a set to store the vertex i have visited
    visited = set()
    #An empty list to store the final value
    result = []
    # use a queue[] to represent queue
    queue = []
    #append strat vertax to queue 
    queue.append(Start)
    # start vertex is visited so i move it to set()
    visited.add(Start)
    # a while loop to determine if there are left stuffs in queue
    while queue:
        # assign the current vertext as the first item in queue
        cur = queue.pop(0)
        #move it into final result list
        result.append(str(cur))
        #iterate to current vertax's neighbors
        for i in cur.neighbors:
            k = g.find_vertex(i)
            if k not in visited:
                # move the neighbors into queue
                visited.add(k)
                queue.append(k)
    #return the result
    return result
    # Perform depth-first search on a directed graph g starting at vertex with label start_label
#return a list a the nodes that visited by DFS
def depthFirst(g, start_label):
    # define the starting vertex by matching its starting label
    start = g.find_vertex(start_label)
    # a set to store the nodes that i have visited
    visited = set()
    # an empty list to store the final result
    result = []
    # input the starting vertex to stack initially
    stack = [start]
    #looping if there are still items in stack
    while stack:
        cur = stack.pop()
        if cur not in visited:
            # add the current vertex to the visited set and result list
            visited.add(cur)
            result.append(str(cur))
            #use a for loop to traversal back to eighbors of current node, the end index is -1, and step is also -1
            for i in range(len(cur.neighbors)-1, -1, -1):
                #find that neighbor, then move it into stack
                neighbor = g.find_vertex(cur.neighbors[i])
                stack.append(neighbor)
    return result
    # return the result
    



if __name__ == "__main__":
# TODO: (Optional) your test code here
    my_graph = Graph()
    vertices = ["0", "1", "2", "3", "4", "5"]
    edges = [["0", "1"], ["0", "2"], ["1", "3"], ["1", "4"], ["2", "5"]]
    for vertex in vertices:
        my_graph.add_vertex(Vertex(vertex))
    for edge in edges:
        my_graph.add_edge(edge[0], edge[1])
    for vertex in my_graph.vertices: # Print out adjacency list
        print("Vertex " , vertex, ":", vertex.neighbors)
    print(breadthFirst(my_graph, "0")) # Correct Output: ["0","1","2","3","4","5"]
    print(depthFirst(my_graph,"0"))