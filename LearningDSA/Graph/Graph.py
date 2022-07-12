class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)
        
    def removeEdge(self,vertex,edge):
        self.gdict[vertex].remove(edge)


customGraph = {"a": ["b", "c"],
               "b": ["a", "d", "e"],
               "c": ["a", "e"],
               "d": ["b", "e", "f"],
               "e": ["d", "f"],
               "f": ["d", "e"]
               }
graph = Graph(customGraph)
graph.addEdge("e", "c")
graph.removeEdge("e", "f")
print(graph.gdict["e"])
