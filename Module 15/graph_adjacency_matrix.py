class Graph:

    def __init__(self, total_vertices):
        self.total_vertices = total_vertices

        self.adjacency_matrix = [
            [0 for column in range(total_vertices)]
            for row in range(total_vertices)
        ]

    def add_edge(self, vertex1, vertex2, weight=1):
        self.adjacency_matrix[vertex1][vertex2] = weight
        self.adjacency_matrix[vertex2][vertex1] = weight

    def get_vertices(self):
        return range(self.total_vertices)

    def get_edges(self):
        edge_list = []

        for row in range(self.total_vertices):
            for column in range(self.total_vertices):

                if self.adjacency_matrix[row][column] != 0:
                    edge_list.append((row, column))

        return edge_list

    def __repr__(self):
        return str(self.adjacency_matrix)


# Create a graph
my_graph = Graph(3)

# Add edges
my_graph.add_edge(0, 1)
my_graph.add_edge(0, 2)
my_graph.add_edge(1, 2)

# Display the graph
print(my_graph)
