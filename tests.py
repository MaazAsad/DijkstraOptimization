# tests.py

import time   

verticesFileNames = ["Vertices.txt"] ## you can add more tests here
edgesFileNames = ["Edges.txt"] ## you can add more tests here

    
import NewDijkstra as nd

## Test the New Dijkstra on the sample file
def new_dijkstra():
    global verticesFileNames
    global edgesFileNames

    for verticesFileName, edgesFileName in zip(verticesFileNames, edgesFileNames):
        g = nd.Graph()

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
        nd.printGraph(g)

    
        start_time = time.time()
        nd.dijkstra(g, g.get_vertex('Seattle'), g.get_vertex('WashingtonDC')) 
        end_time = time.time()

        destination = g.get_vertex('WashingtonDC')
        path = [destination.get_id()]
        nd.shortest_path(destination, path)    

        # assert path[::-1] == ['Seattle', 'Minneapolis', 'Chicago', 'WashingtonDC'] 

        print("============= Time Taken =", end_time-start_time, "=============")

        print ("Shortest path is ", path[::-1])
        
        return path[::-1]





import BasicDijkstra as bd

## Test the basic Dijkstra on the sample file    
def basic_dijkstra():
    global verticesFileNames
    global edgesFileNames

    for verticesFileName, edgesFileName in zip(verticesFileNames, edgesFileNames):
        g = bd.Graph()

        ## Read vertices from a file
        with open(verticesFileName,"r") as fp:
            lines = fp.readlines()
            for line in lines:
                g.add_vertex(line.strip())


        ## Read edges from a file
        with open(edgesFileName,"r") as fp:
            lines = fp.readlines()
            for line in lines:
                x = line.split(',')
                g.add_edge( x[0].strip(), x[1].strip(), float(x[2].strip()))


        ## print Graph
        bd.printGraph(g)

    
        start_time = time.time()
        bd.dijkstra(g, g.get_vertex('Seattle'), g.get_vertex('WashingtonDC')) 
        end_time = time.time()

        destination = g.get_vertex('WashingtonDC')
        path = [destination.get_id()]
        bd.shortest_path(destination, path)    

        # assert path[::-1] == ['Seattle', 'Minneapolis', 'Chicago', 'WashingtonDC'] 

        print ("Shortest path is ", path[::-1])

        print("============= Time Taken =", end_time-start_time, "=============")

        return path[::-1]

def test_bothEqual():
    assert basic_dijkstra() == new_dijkstra()