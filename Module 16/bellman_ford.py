# Python program for Bellman-Ford's single-source
# shortest path algorithm


# Class to represent a graph
class Graph:

    def __init__(self, total_vertices):
        self.total_vertices = total_vertices

        # Store edges as:
        # [source, destination, weight]
        self.edges = []

    # Add an edge to the graph
    def add_edge(self, source_vertex, destination_vertex, edge_weight):
        self.edges.append(
            [source_vertex, destination_vertex, edge_weight]
        )

    # Display the shortest distances
    def print_solution(self, distances):

        print("Vertex\tDistance from Source")

        for vertex in range(self.total_vertices):
            print(
                "{0}\t\t{1}".format(
                    vertex,
                    distances[vertex]
                )
            )

    # Bellman-Ford algorithm
    def bellman_ford(self, source_vertex):

        # Step 1:
        # Initially, the distance from the source to every
        # vertex is infinity
        distances = [float("Inf")] * self.total_vertices

        # Distance from source to itself is 0
        distances[source_vertex] = 0

        # Step 2:
        # Relax all edges (V - 1) times
        for _ in range(self.total_vertices - 1):

            for source, destination, weight in self.edges:

                # Relax the edge if a shorter path is found
                if (
                    distances[source] != float("Inf")
                    and distances[source] + weight
                    < distances[destination]
                ):
                    distances[destination] = (
                        distances[source] + weight
                    )

        # Step 3:
        # Check for a negative-weight cycle
        for source, destination, weight in self.edges:

            if (
                distances[source] != float("Inf")
                and distances[source] + weight
                < distances[destination]
            ):
                print("Graph contains negative weight cycle")
                return

        # Display the shortest distances
        self.print_solution(distances)


# Driver code
if __name__ == "__main__":

    # Create a graph with 5 vertices
    my_graph = Graph(5)

    # Add edges
    my_graph.add_edge(0, 1, -1)
    my_graph.add_edge(0, 2, 4)
    my_graph.add_edge(1, 2, 3)
    my_graph.add_edge(1, 3, 2)
    my_graph.add_edge(1, 4, 2)
    my_graph.add_edge(3, 2, 5)
    my_graph.add_edge(3, 1, 1)
    my_graph.add_edge(4, 3, -3)

    # Find shortest paths from vertex 0
    my_graph.bellman_ford(0)
