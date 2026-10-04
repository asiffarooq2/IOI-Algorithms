# Iterative DFS traversal of a directed graph
# using an adjacency list and a stack


class Graph:

    def __init__(self, total_vertices):
        # Total number of vertices
        self.total_vertices = total_vertices

        # Create an empty adjacency list for each vertex
        self.adjacency_list = [
            [] for vertex in range(total_vertices)
        ]

    # Add a directed edge to the graph
    def add_edge(self, source_vertex, destination_vertex):
        self.adjacency_list[source_vertex].append(destination_vertex)

    # Perform DFS traversal from a starting vertex
    def depth_first_search(self, start_vertex):

        # Initially, mark all vertices as not visited
        visited_vertices = [
            False for vertex in range(self.total_vertices)
        ]

        # Create a stack for DFS
        vertex_stack = []

        # Add the starting vertex to the stack
        vertex_stack.append(start_vertex)

        # Continue until the stack becomes empty
        while len(vertex_stack):

            # Remove the top vertex from the stack
            current_vertex = vertex_stack.pop()

            # Visit the vertex if it has not been visited
            if not visited_vertices[current_vertex]:

                print(current_vertex, end=" ")
                visited_vertices[current_vertex] = True

            # Get all neighboring vertices
            for neighbor_vertex in self.adjacency_list[current_vertex]:

                # Add unvisited neighbors to the stack
                if not visited_vertices[neighbor_vertex]:
                    vertex_stack.append(neighbor_vertex)


# Create a graph with 5 vertices
my_graph = Graph(5)

# Add edges
my_graph.add_edge(0, 2)
my_graph.add_edge(0, 1)
my_graph.add_edge(1, 2)
my_graph.add_edge(2, 0)
my_graph.add_edge(2, 3)
my_graph.add_edge(3, 3)


# Perform DFS traversal
print("Following is Depth First Traversal:")
my_graph.depth_first_search(0)
