
class Node:
    def __init__(self, id, id_osm, lon, lat):
        self.id = id
        self.id_osm = id_osm
        self.lon = lon
        self.lat = lat

class Edge:
    def __init__(self, id, source, target, longitud):
        self.id = id
        self.source = source
        self.target = target
        self.longitud = longitud

class Atribute:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class AdjNode:
    def __init__(self, value):
        self.vertex = value 
        self.next = None

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V
        
    def add_edge(self, src, target):
        node = AdjNode(target)
        node.next = self.graph[src]
        self.graph[src] = node


    def print_adjList(self):
        for i in range(self.V):
            print("Vertex " + str(i) + ":", end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")


