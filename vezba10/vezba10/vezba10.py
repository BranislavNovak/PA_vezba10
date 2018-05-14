from enum import Enum	
import math
import random
import string

class Vertex:
    """
    Graph vertex: A graph vertex (node) with data
    """
    def __init__(self, c = None, p = None, d1 = None, d2 = None):
        """
        Vertex constructor 
        @param color, parent, auxilary data1, auxilary data2
        """
        self.c = c
        self.p = p
        self.d1 = d1
        self.d2 = d2
        self.list = list()

	
class Edge:
    def __init__(self, source = None, destination = None, weight = None):
        self.source = source;
        self.destination = destination
        self.weight = weight

class VertexColor(Enum):
        BLACK = 0
        GRAY = 127
        WHITE = 255		

def initialize_single_source(G,s):
    for v in G:
        v.d1 = math.inf
        v.p = None
    s.d1 = 0

def relax(u, v, w):    
    if v.d1 > u.d1 + w:
        v.d1 = u.d1 + w
        v.p = u

def extract_min(Q):
    min = 0
    for i in range (len(Q)):
        if Q[i].d1 <= Q[min].d1:
            min = i
    ret = Q.pop(min)
    return ret

def dijkstra(G, w, s):
    initialize_single_source(G,s)
    S = list()
    Q = G[:]
    while len(Q) is not 0:
        u = extract_min(Q)
        print("min in the moment: -------->", u.d2)
        S.append(u)
        for v in u.list:
            relax(v.source, v.destination, v.weight)
   

def print_vertex(v):
    for i in v:
        print(" --------->", i.d2, " = ", i.d1)
        for j in i.list:
            print(j.destination.d2, " weight", j.weight)

def generate_random_graph():
    number_of_vertexes = random.randint(5, 20)
    vertex_list = []
    for i in range(1, number_of_vertexes + 1):
        #print("Adding vertexes to list!")
        vertex_list.append(Vertex(d2 = i))
    for vertex in vertex_list:
        #print("Adding edges to each vertex!")
        number_of_edges = random.randint(0, number_of_vertexes)
        for i in range(0, number_of_edges):
            #print("Adding source, destination and weight on each edge!")
            vertex.list.append(Edge(source = vertex, destination = vertex_list[random.randint(0, number_of_vertexes-1)], weight = random.randint(0, 20)))
    return vertex_list

if __name__ == "__main__":
    vertex_list = list()
    s = Vertex(d2 = 's')
    t = Vertex(d2 = 't')
    x = Vertex(d2 = 'x')
    y = Vertex(d2 = 'y')
    z = Vertex(d2 = 'z')

    s.list.append(Edge(s, t, 10))
    s.list.append(Edge(s, y, 5))

    t.list.append(Edge(t, x, 1))    
    t.list.append(Edge(t, y, 2))
    
    x.list.append(Edge(x, z, 4))
    
    
    y.list.append(Edge(y, t, 3))
    y.list.append(Edge(y, x, 9))
    y.list.append(Edge(y, z, 2))

    z.list.append(Edge(z, s, 7))
    z.list.append(Edge(z, x, 6))

    vertex_list.append(s)
    vertex_list.append(t)
    vertex_list.append(x)
    vertex_list.append(y)
    vertex_list.append(z)
    
    print_vertex(vertex_list)

    dijkstra(vertex_list, 0, s)

    vertex_list.append(s)
    vertex_list.append(t)
    vertex_list.append(x)
    vertex_list.append(y)
    vertex_list.append(z)

    print_vertex(vertex_list)


    print("\n---------random graph----------\n")
   
    vertex_list_rand = generate_random_graph()
   
    for i in vertex_list_rand:
        print(i.d2)
        for j in i.list:
            print(j.destination.d2, " weight", j.weight)

    dijkstra(vertex_list_rand, 0, vertex_list_rand[0])
    
    print_vertex(vertex_list_rand)
    

