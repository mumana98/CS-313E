import os

#stack class -----------------------------------------------------------------------------------------------------
class Stack (object):
    def __init__ (self):
        self.stack = []

    # add an item to the top of the stack
    def push (self, item):
        self.stack.append (item)

    # remove an item from the top of the stack
    def pop (self):
        return self.stack.pop()

    # check the item on the top of the stack
    def peek (self):
        return self.stack[-1]

    # check if the stack if empty
    def is_empty (self):
        return (len (self.stack) == 0)

    # return the number of elements in the stack
    def size (self):
        return (len (self.stack))

#queue class -----------------------------------------------------------------------------------------------------
class Queue (object):
    def __init__ (self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue (self, item):
        self.queue.append (item)

    # remove an item from the beginning of the queue
    def dequeue (self):
        return (self.queue.pop(0))

    # check if the queue is empty
    def is_empty (self):
        return (len (self.queue) == 0)

    # return the size of the queue
    def size (self):
        return (len (self.queue))

#vertex class -----------------------------------------------------------------------------------------------------
class Vertex (object):
    def __init__ (self, label):
        self.label = label
        self.visited = False

    # determine if a vertex was visited
    def was_visited (self):
        return self.visited

    # determine the label of the vertex
    def get_label (self):
        return self.label

    # string representation of the vertex
    def __str__ (self):
        return str (self.label)

#graph class -----------------------------------------------------------------------------------------------------
class Graph (object):
    def __init__ (self):
        self.Vertices = []
        self.adjMat = []

    # check if a vertex is already in the graph
    def has_vertex (self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if label == (self.Vertices[i]).get_label():
                return True
        return False

    # get the index from the vertex label
    def get_index (self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if label == (self.Vertices[i]).get_label():
                return i
        return -1

    # add a Vertex object with a given label to the graph
    def add_vertex (self, label):
        if not self.has_vertex(label):
            self.Vertices.append(Vertex(label))

        nVert = len(self.Vertices)

        for i in range(nVert-1):
            self.adjMat[i].append(0)

        new_row = []

        for i in range(nVert):
            new_row.append(0)

        self.adjMat.append(new_row)

    # add weighted directed edge to graph
    def add_directed_edge (self, start, finish, weight = 1):
        self.adjMat[start][finish] = weight

    # add weighted undirected edge to graph
    def add_undirected_edge (self, start, finish, weight = 1):
        self.adjMat[start][finish] = weight
        self.adjMat[finish][start] = weight

    # get edge weight between two vertices
    # return -1 if edge does not exist
    def get_edge_weight (self, fromVertexLabel, toVertexLabel):
        weight = self.adjMat[self.get_index(fromVertexLabel)][self.get_index(toVertexLabel)]
        if weight:
            return weight
        else:
            return -1

    # get a list of immediate neighbors that you can go to from a vertex
    # return a list of indices or an empty list if there are none
    def get_neighbors (self, vertexLabel):
        nVert = len (self.Vertices)
        v = self.get_index(vertexLabel)
        neighbors = []
        for i in range (nVert):
            if (self.adjMat[v][i] > 0):
                neighbors.append(i)
        #print("NEIGHBORS:", neighbors)
        return neighbors

    # return an index to an unvisited vertex adjacent to vertex v (index)
    def get_adj_unvisited_vertex (self, v):
        nVert = len (self.Vertices)
        for i in range (nVert):
            if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
                return i
        return -1

    # get a copy of the list of Vertex objects
    def get_vertices (self):
        return self.Vertices

    # do a depth first search in a graph starting at vertex v (index)
    def dfs (self, v):
        # create the Stack
        theStack = Stack ()

        # mark the vertex v as visited and push it on the Stack
        (self.Vertices[v]).visited = True
        print (self.Vertices[v])
        theStack.push (v)

        # visit all the other vertices according to depth
        while (not theStack.is_empty()):
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex (theStack.peek())
            if (u == -1):
                u = theStack.pop()
            else:
                (self.Vertices[u]).visited = True
                print (self.Vertices[u])
                theStack.push (u)

        # the stack is empty, let us rest the flags
        nVert = len (self.Vertices)
        for i in range (nVert):
            (self.Vertices[i]).visited = False

    # do a breadth first search in a graph starting at vertex v (index)
    def bfs (self, v):
        the_queue = Queue()
        self.Vertices[v].visited = True

        the_queue.enqueue(v)

        while (not the_queue.is_empty()):
            dq = self.Vertices[the_queue.dequeue()]
            #print("Dequeued", dq)
            print(dq)
            neighbors = self.get_neighbors(str(dq))
            #print("ATs neighbors:",self.get_neighbors("Atlanta"))
            #print(dq,"NEIGHBORS:", neighbors)
            
            for neighbor in neighbors:
                if self.Vertices[neighbor].visited == False:
                    self.Vertices[neighbor].visited = True
                    the_queue.enqueue(neighbor)
                    #print("neighbor enqueued",the_queue.enqueue(neighbor))
            #print("Q's q:",the_queue.queue)
                    #print (neighbor)
            '''
            for i in the_queue.queue:
                print(i.get_label(), end=" ")
            print()
            '''

        nVert = len (self.Vertices)
        for i in range (nVert):
            (self.Vertices[i]).visited = False

    # delete an edge from the adjacency matrix
    # delete the edge if the graph is going from start to finish
    def delete_edge (self, fromVertexLabel, toVertexLabel):
        self.adjMat[self.get_index(fromVertexLabel)][self.get_index(toVertexLabel)] = 0
        self.adjMat[self.get_index(toVertexLabel)][self.get_index(fromVertexLabel)] = 0

    # delete a vertex from the vertex list and all edges from and
    # to it in the adjacency matrix
    def delete_vertex (self, vertexLabel):
        for i in self.get_neighbors(vertexLabel):
            self.delete_edge(vertexLabel, str(self.Vertices[i]))
        del self.Vertices[self.get_index(vertexLabel)]

#main -----------------------------------------------------------------------------------------------------------
def main():
    # create the Graph object
    cities = Graph()

    # open the file for reading
    num_vertices = eval(input())
    #print(num_vertices)

    # read the vertices to the list of Vertices
    for i in range (num_vertices):
        city = input().strip()
        #print (city)
        cities.add_vertex(city)

    # read the number of edges
    num_edges = int((input()).strip())
    #print (num_edges)

    # read each edge and place it in the adjacency matrix
    for i in range (num_edges):
        edge = (input()).strip()
        #print (edge)
        edge = edge.split()
        start = int (edge[0])
        finish = int (edge[1])
        weight = int (edge[2])

        cities.add_directed_edge (start, finish, weight)

    # read the starting vertex for dfs and bfs
    start_vertex = input()
    
    # get the index of the starting vertex
    start_index = cities.get_index (start_vertex)
    '''
    for i in cities.get_neighbors("Atlanta"):
        print("Neighbors of Atlanta:",i)
    '''
    # do the depth first search
    print ("Depth First Search")
    cities.dfs (start_index)
    print ()
    
    # test breadth first search
    print ("Breadth First Search")
    cities.bfs (start_index)
    print ()

    # test deletion of an edge
    print ("Deletion of an edge")
    #print(input().strip())
    e = input().split()
    cities.delete_edge(e[0], e[1])

    print ("\nAdjacency Matrix")
    for i in range (num_vertices):
        for j in range (num_vertices):
            print (cities.adjMat[i][j], end = " ")
        print ()
    print ()

    # test deletion of a vertex
    print ("Deletion of a vertex")
    print()
    print ("List of Vertices")
    dv = input()
    dvi = cities.get_index(str(dv))
    cities.delete_vertex(dv)
    for i in cities.Vertices:
        i.get_label()
        print(i)

    print ("\nAdjacency Matrix")
    for i in range (num_vertices):
        if i == dvi:
            continue
        for j in range (num_vertices):
            if j == dvi:
                continue
            print (cities.adjMat[i][j], end = " ")
        print ()

main()