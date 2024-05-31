class graphAdjacencyList:
    def __init__(self):
        self.graph= {}

    def add_vertex(self,v):
        if v not in self.graph:
            self.graph[v]=[]

    def add_edges(self,v1,v2):
        if v1 in self.graph:
            self.graph[v1].append(v2)
        else:
            self.graph[v1] = v2
        if v2 in self.graph:
            self.graph[v2].append(v1)
        else:
            self.graph[v2]=v1

    def display(self):
        for vertex in self.graph:
            for neighbour in self.graph[vertex]:
                print('(',vertex,',',neighbour,')')

graph = graphAdjacencyList()
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_edges(1, 2)
graph.add_edges(2,3)
graph.add_edges(3, 1)
graph.display()
