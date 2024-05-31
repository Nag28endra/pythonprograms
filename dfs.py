class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self,v):
        self.graph[v]=[]

    def add_edges(self,v1,v2):
        if v1 in self.graph:
            self.graph[v1].append(v2)

        else: 
            self.graph[v1]=[v2]
        if v2 in self.graph:
            self.graph[v2].append(v1)
        else:
            self.graph[v2]=[v1]

    def display(self):
        for vertex in self.graph:
            for neighbour in self.graph[vertex]:
                print('(',vertex,',',neighbour,')')

    def dfs(self,vertex):
        visited = set()
        self.recursiveDFS(visited,vertex)

    def recursiveDFS(self,visited,vertex):
        visited.add(vertex)
        print(vertex,end=" ")

        for vertext in self.graph:
            for neighbour in self.graph[vertex]:
                if neighbour not in visited:
                    self.recursiveDFS(visited, neighbour)

dfs = Graph()
dfs.add_vertex(1)
dfs.add_vertex(2)
dfs.add_vertex(3)
dfs.add_vertex(4)
dfs.add_edges(1, 2)
dfs.add_edges(2,3)
dfs.add_edges(3,4)
dfs.display()
dfs.dfs(1)