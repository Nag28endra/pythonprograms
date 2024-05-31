import numpy as np

class graphAdjacency:
    def __init__(self,vertices):
        self.vertices = vertices
        # self.graph = [[0]*vertices for _ in range(vertices)]
        self.graph = np.zeros((vertices,vertices),dtype=int)

    def add_edges(self,v1,v2):
        
        self.graph[v1][v2]=1
        
        self.graph[v2][v1]=1

    def display(self):
        for row in self.graph:
            print(row)

graph = graphAdjacency(4)
graph.add_edges(1, 2)
graph.add_edges(2, 3)
graph.add_edges(3, 0)
graph.add_edges(0, 1)
graph.display()