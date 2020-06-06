import sys
import time #for execution times

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        # Set distance to infinity for all nodes
        self.distance = float("inf")
        # Mark all nodes unvisited        
        self.visited = False  
        # Predecessor
        self.previous = None

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])
    
    #Operator overloading
    def __lt__(self, other):
        return (self.distance < other.distance)

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous

def shortest_path(v, path):
    ''' make shortest path from v.previous'''
    if v.previous:
        path.append(v.previous.get_id())
        shortest_path(v.previous, path)
    return

import heapq

def dijkstra(aGraph, start, target):
    print("\n\n")
    print (''' # # # # #     Basic Dijkstra's shortest path     # # # # #''')
    # Set the distance for the start node to zero 
    start.set_distance(0)

    # Put tuple pair into the priority queue
    unvisited_queue = [(v.get_distance(),v) for v in aGraph]
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
            new_dist = current.get_distance() + current.get_weight(next)
            
            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)
                fmt = '{0:<30}: {1:>10.2f} (Updated)'
                print (fmt.format(current.get_id() + " -> " + next.get_id(), next.get_distance()))
            else:
                fmt = '{0:<30}= {1:>10.2f} (Not Updated)'
                print (fmt.format(current.get_id() + " -> " + next.get_id(), next.get_distance()))

        # Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v.get_distance(),v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)
    

def printGraph(g):
    print ('\n')
    print ('The Graph is:')
    for vertex in g:
        for w in vertex.get_connections():
            v_id = vertex.get_id()
            w_id = w.get_id()
            fmt = '{0:<30} --- {1:>10.2f}'
            print (fmt.format(v_id + " -> " + w_id, vertex.get_weight(w)))
        
if __name__ == '__main__':

    g = Graph()

     ## READ  Vertices file
    fileHandle = open("Vertices.txt","r")

    for lines in fileHandle:
        g.add_vertex( lines.strip())

    fileHandle.close()


    ## READ Egdes file

    fileHandle = open("Edges.txt","r")

    for lines in fileHandle:
        x = lines.split(',')
        g.add_edge( x[0].strip(), x[1].strip(), float(x[2].strip()))

    fileHandle.close()


    start_time = time.time()

    dijkstra(g, g.get_vertex('Seattle'), g.get_vertex('WashingtonDC')) 

    target = g.get_vertex('WashingtonDC')
    path = [target.get_id()]
    shortest_path(target, path)
    print ('The shortest path : %s' %(path[::-1]))
    print("--- %s seconds ---" % (time.time() - start_time))