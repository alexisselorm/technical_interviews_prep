class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def removeEdge(self, vertex, edge):
        if edge in self.gdict[vertex]:
            self.gdict[vertex].remove(edge)
            return "edge removed"
        return "No connection between edge and vertex"

    def removeVertex(self, vertex):
        if vertex in self.gdict.keys():
            for edges in self.gdict[vertex]:
                self.gdict[edges].remove(vertex)
            del self.gdict[vertex]
            return True
        return False


customGraph = {"a": ["b", "c"],
               "b": ["a", "d", "e"],
               "c": ["a", "e"],
               "d": ["b", "e", "f"],
               "e": ["d", "f"],
               "f": ["d", "e"]
               }
graph = Graph(customGraph)
graph.addEdge("e", "c")
print(graph.removeEdge("e", "a"))
print(graph.removeVertex("f"))
print(graph.gdict)
