
import pandas as pd
import numpy as np
import time


## Struct which holds Attributes and Functions of the Vertex
# = = = = = = = VERTEX STRUCTURE = = = = = = = #
class Vertex:
    def __init__(self, Node, Latitude, Longitude):
        self.id = Node
        self.adjacent = {} # toDo: use Numpy dict

        self.distance = float("inf") # Set distance to infinity for this Node by default
        self.visited = False # Mark this Node unvisited by default        
        self.previous = None  # The Node before it, set to None by default

        ## Latitude and Longitude
        self.Latitude = Latitude
        self.Longitude = Longitude

## - - - - - - - GETTERS AND SETTERS - - - - - - - ## 
    def get_id(self):
        return self.id

    def get_connections(self):
        return self.adjacent.keys()  

    def get_edge_weight(self, neighbor):
        return self.adjacent[neighbor]

    def get_visited(self):
        return self.visited

    def get_Latitude(self):
        return self.Latitude
    
    def get_Longitude(self):
        return self.Longitude

    def get_distance(self):
        return self.distance

    def set_distance(self, dist):
        self.distance = dist

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True


## - - - - - - - FUNCTIONS - - - - - - - ##
    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def has_neighbor(self, neighbor):
        if neighbor in self.adjacent:
            return True
        return False

## - - - - - - - OPERATOR OVERLOADING - - - - - - - ##
    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])
    
    def __lt__(self, other):
        return (self.distance < other.distance)




## Struct which holds Attributes and Functions of the Graph
# = = = = = = = GRAPH STRUCTURE = = = = = = = #
class Graph:
    def __init__(self):
        self.vert_dict = {} #toDo: use numpy dict
        self.Number_Of_Vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

## - - - - - - - GETTERS AND SETTERS - - - - - - - ## 
    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def get_vertices(self):
        return self.vert_dict.keys()

    def get_previous(self, current):
        return self.previous

    def set_previous(self, current):
        self.previous = current


## - - - - - - - FUNCTIONS - - - - - - - ##
    def add_edge(self, Source, Destination, Cost = 0):
        if Source not in self.vert_dict:
            print("Source %s Node not present\n" % (Source))
            return
        if Destination not in self.vert_dict:
            print("Destination %s Node not present\n" % (Destination))
            return

        self.vert_dict[Source].add_neighbor(self.vert_dict[Destination], Cost)
        self.vert_dict[Destination].add_neighbor(self.vert_dict[Source], Cost)

    def add_vertex(self, Node, Latitude, Longitude):
        self.Number_Of_Vertices = self.Number_Of_Vertices + 1
        new_vertex = Vertex(Node,Latitude,Longitude)
        self.vert_dict[Node] = new_vertex
        return new_vertex



## Utility function which recursively builds the shortest path
# based on the previous values in the path
def shortest_path(v, path):
    if v.previous:
        path.append(v.previous.get_id())
        shortest_path(v.previous, path)
    return



import math
import heapq

def dijkstra(theGraph, Start, End):
    print ('''Dijkstra's shortest path''')

    #Constraint Weights
    Omega_u = float(1000)
    AngleLowerBound = -0.5 * math.pi
    AngleUpperBound = 0.5 * math.pi


    # Set the distance for the start Node to zero 
    Start.set_distance(0)
    Start.set_visited()
    source_Latitude = Start.get_Latitude()
    source_Longitude = Start.get_Longitude()

    dest_Latitude = End.get_Latitude()
    dest_Longitude = End.get_Longitude()

    x1 = dest_Latitude - source_Latitude 
    y1 = dest_Longitude - source_Longitude 

    # Put tuple pair into the priority queue
    unvisited_queue = [(v.get_distance(),v) for v in theGraph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        # Pops a vertex with the smallest distance 
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()

        #for next in v.adjacent:
        for next in current.adjacent:
            # if visited, skip
            if next.visited:
                continue

            curr_Latitude = next.get_Latitude()
            curr_Longitude = next.get_Longitude()

            x2 = curr_Latitude - source_Latitude 
            y2 = curr_Longitude - source_Longitude 

            x = x1 * x2 + y1* y2
            y = math.sqrt( pow(x1,2) + pow(y1,2) ) * math.sqrt( pow(x2,2) + pow(y2,2) )

            x = x/y

            if(AngleLowerBound < x and  x < AngleUpperBound):
                new_weight = Omega_u * x
                new_dist = current.get_distance() + current.get_edge_weight(next) + new_weight
                
                if new_dist < next.get_distance():
                    next.set_distance(new_dist)
                    next.set_previous(current)
                    print ('updated : current = %s next = %s new_dist = %s' % (current.get_id(), next.get_id(), next.get_distance()))
                else:
                    print ('not updated : current = %s next = %s new_dist = %s' %(current.get_id(), next.get_id(), next.get_distance()))

        # Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v.get_distance(),v) for v in theGraph if not v.visited]
        heapq.heapify(unvisited_queue)
    

def printGraph(g):
    print ('The Graph is:')
    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print ('( %s -> %s\t\t%3d)'  % ( vid, wid, v.get_edge_weight(w)))
        

# Main Function
def main(verticesFileName, edgesFileName):
    g = Graph()

    ## Read vertices from a file
    with open(verticesFileName,"r") as fp:
        lines = fp.readlines()
        for line in lines:
            x = line.split(',')
            g.add_vertex( x[0].strip(), float(x[1].strip()), float(x[2].strip()) )


    ## Read edges from a file

    with open(edgesFileName,"r") as fp:
        lines = fp.readlines()
        for line in lines:
            x = line.split(',')
            g.add_edge( x[0].strip(), x[1].strip(), float(x[2].strip()))


    ## print Graph
    printGraph(g)

   
    start_time = time.time()
    dijkstra(g, g.get_vertex('Seattle'), g.get_vertex('WashingtonDC')) 
    end_time = time.time()


    destination = g.get_vertex('WashingtonDC')
    path = [destination.get_id()]
    shortest_path(destination, path)
    print ('The shortest path : %s' %(path[::-1]))
    print("--- %s seconds ---" % (end_time - start_time))
    return path[::-1];

main("Vertices.txt", "Edges.txt")