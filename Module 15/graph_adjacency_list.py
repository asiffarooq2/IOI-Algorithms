# A graph data structure using adjacency list

class Graph:

    def __init__(self, total_vertices):
        self.total_vertices = total_vertices
        self.adjacency_list = [[vertex] for vertex in range(total_vertices)]

    def add_edge(self, source, destination):
        self.adjacency_list[source].append(destination)

    def display_graph(self):
        for vertex in range(self.total_vertices):
            print(vertex, "->", self.adjacency_list[vertex])


# Create a graph with 5 vertices
my_graph = Graph(5)

# Add edges
my_graph.add_edge(0, 1)
my_graph.add_edge(0, 2)
my_graph.add_edge(1, 2)
my_graph.add_edge(2, 3)
my_graph.add_edge(3, 4)

# Display the graph
my_graph.display_graph()
