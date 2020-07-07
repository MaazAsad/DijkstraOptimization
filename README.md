# DijkstraOptimization
![Python application](https://github.com/MaazAsad/DijkstraOptimization/workflows/Python%20application/badge.svg)
Algorithms Project, Batch 18.

## Abstract
The Algorithm we were to implement was "An Improved Dijkstra Shortest Path Algorithm" by Yizhen Huang, Qingming Yi, and Min Shi of College of Information Science and Technology, Jinan University, Guangzhou, China. As the name suggests, it is an improvement over the basic data structure based Dijkstra algorithm, by using a search strategy based technique. In this technique, based on the angle between the vector of current path and desired path, the algorithm rules out unnecessary paths.

## Tools Used
- Python 3.7+
- Numpy
- Pytest and GitHub Actions for CI Testing

## How to Run
After installing pytest and numpy via
>        pip install flake8 pytest
>        pip install numpy

Run the test program with
>        pytest tests.py -vv --durations=2 -s 

Or the separate algorithms
>        python BasicDijkstra.py
>        python NewDijkstra.py


## How to create a sample file
Structure the Vertices as given in Vertices.txt in one file, and structure the Edges as given in Edges.txt in another file (The structure is determined for the new Dijkstra Algorithm, the old one ignore the Lat/Long values). The current sample file represents the below graph:

![Sample graph](usa.png?raw=true)

Then add the filenames in the arrays in pytest, called "verticesFileNames" and "edgesFileNames".
