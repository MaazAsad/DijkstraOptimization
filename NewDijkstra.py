#REQUIRMENTS
'''
both source and end nodes should exist before creation of edge between them
atleast 1 path exists between the source and target node
'''

import time #for execution times

class Vertex:
    def __init__(self, node,Lat,Longitude):
        self.id = node
        self.adjacent = {}
        # Set distance to infinity for all nodes
        self.distance = float("inf")
        # Mark all nodes unvisited        
        self.visited = False  
        # Predecessor
        self.previous = None

        ##Latitude and longitude
        self.Lattitude = Lat
        self.Longitude = Longitude

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def has_neighbor(self,neighbor):
        if neighbor in self.adjacent:
            return True
        return False

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
    
    
    def get_visited(self):
        return self.visited


    def get_Lattitude(self):
        return self.Lattitude
    
    def get_Longitude(self):
        return self.Longitude

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

    def add_vertex(self, node,Latitude,Longitude):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node,Latitude,Longitude)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            print("Source %s node not present\n" % (frm))
            return
        if to not in self.vert_dict:
            print("Destination %s node not present\n" % (to))
            return

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous


def shortest(v, path):
    ''' make shortest path from v.previous'''
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return



import math

def Dijkstra(Graph,Start,End):
    #yolo
    #constraint weight
    Omega_u = float(2000)
    AngleLowerBound = -0.5 * math.pi
    AngleUpperBound = 0.5 * math.pi

    Start.set_distance(0)

    openList = Start.get_connections()
    source = Start
    source.set_visited()
    source_lattitude = Start.get_Lattitude()
    source_longitude = Start.get_Longitude()

    dest_lattitude = End.get_Lattitude()
    dest_longitude = End.get_Longitude()

    x1 = dest_lattitude - source_lattitude
    y1 = dest_longitude - source_longitude
    counter =0

    while len(openList):

        print("Exec %d" %(counter))
        a = input()
        counter+=1

        #update weights of the edges based on new constraint
        for i in openList:            
            if(i.get_id() != Start.get_id()):
                curr_lattitude = i.get_Lattitude()
                curr_longitude = i.get_Longitude()

                x2 = source_lattitude - curr_lattitude
                y2 = source_longitude - curr_longitude

                x = x1 * x2 + y1* y2
                y = math.sqrt( pow(x1,2) + pow(y1,2) ) * math.sqrt( pow(x2,2) + pow(y2,2) )

                x = x/y
                if(AngleLowerBound < x and  x < AngleUpperBound):
                    new_weight = Omega_u * x
                    new_weight =  source.get_weight(i) + new_weight

                    print("Updating weight for %s" %(i.get_id()))
                    if ( new_weight < i.get_distance() ):
                        
                        i.set_distance(new_weight)
                        i.set_visited()
                        i.set_previous(source.get_id())

        
        #select minimum weighted egde
        temp = list(openList)[0]
        for i in openList:
            if (temp.get_distance() < i.get_distance()  and i.get_id() != Start.get_id()):
                temp = i

        print("Minumum node: %s with weight %s " % (temp.get_id(), temp.get_distance()))
        #check if thee minimum node is the target node
        if(temp.get_id() == End):
            return
        
        source = Graph.get_vertex(temp.get_id())
        openList = source.get_connections()
        

        

        







# Main Function
if __name__ == "__main__":

    g = Graph()

    ## READ  Vertices file
    fileHandle = open("Vertices.txt","r")

    for lines in fileHandle:
        x = lines.split(',')
        g.add_vertex( x[0].strip(), float(x[1].strip()), float(x[2].strip()) )

    fileHandle.close()


    ## READ Egdes file

    fileHandle = open("Edges.txt","r")

    for lines in fileHandle:
        x = lines.split(',')
        g.add_edge( x[0].strip(), x[1].strip(), float(x[2].strip()))

    fileHandle.close()



    ## Display Graph
    print ('Graph data:')
    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print ('( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w)))




    start_time = time.time()

    Dijkstra(g, g.get_vertex('Seattle'), g.get_vertex('WashingtonDC')) 

    end_time = time.time()
    target = g.get_vertex('WashingtonDC')
    path = [target.get_id()]
    shortest(target, path)
    print ('The shortest path : %s' %(path[::-1]))
    print("--- %s seconds ---" % (end_time - start_time))