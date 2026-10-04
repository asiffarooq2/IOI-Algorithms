class Graph:

    def __init__(self):
        self.vertices = set()
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        self.vertices.add(vertex)

    def add_edge(self, vertex1, vertex2, weight=1):

        if vertex1 not in self.vertices:
            self.vertices.add(vertex1)

        if vertex2 not in self.vertices:
            self.vertices.add(vertex2)

        if vertex1 not in self.adjacency_list:
            self.adjacency_list[vertex1] = set()

        self.adjacency_list[vertex1].add((vertex2, weight))

        if vertex2 not in self.adjacency_list:
            self.adjacency_list[vertex2] = set()

        self.adjacency_list[vertex2].add((vertex1, weight))

    def get_vertices(self):
        return self.vertices

    def get_adjacency_list(self):
        return self.adjacency_list

    def __repr__(self):
        return str(self.vertices) + " -> " + str(self.adjacency_list)


# Create a graph
my_graph = Graph()

# Add vertices
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")

# Add edges
my_graph.add_edge("A", "B")
my_graph.add_edge("A", "C")
my_graph.add_edge("B", "C")

# Display the graph
print(my_graph)