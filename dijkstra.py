import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self,u,v,priority):
        if u not in self.graph:
            self.graph[u]=[]
        if v not in self.graph:
            self.graph[v]=[]
        self.graph[u].append((v,priority))
        self.graph[v].append((u,priority))

    def dijkistra(self,source):
        distances = {vertex:float('inf') for vertex in self.graph}
        previous = {vertex:None for vertex in self.graph}
        distances[source]=0

        priority_queue = [(0,source)]

        while priority_queue:
            dist,vertex = heapq.heappop(priority_queue)

            if dist>distances[vertex]:
                continue

            for neighbour,weight in self.graph[vertex]:
                newDistance = dist+weight
                if newDistance<distances[neighbour]:
                    distances[neighbour]= newDistance
                    previous[neighbour]= vertex
                    heapq.heappush(priority_queue,(newDistance,neighbour))

        return previous,distances

    def display(self,source):
        previous,distances = self.dijkistra(source)

        for vertex in self.graph:
            path = []
            current_vertex = vertex

            while current_vertex is not None:
                path.append(current_vertex)
                current_vertex = previous[current_vertex]

            path.reverse()
            print(f'the shortest path of {source} to {vertex} is {path} distance:{distances[vertex]}')

graph = Graph()
graph.add_edge('A', 'B', 5)
graph.add_edge('B', 'C', 1)
graph.add_edge('A', 'C', 3)
graph.add_edge('B', 'D', 4)
graph.add_edge('C','E', 1)
graph.add_edge('D', 'E', 6)
graph.add_edge('C', 'D', 8)

graph.display('A')