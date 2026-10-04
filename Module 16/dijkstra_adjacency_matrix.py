# Python program for Dijkstra's single-source
# shortest path algorithm using an adjacency matrix

import sys


class Graph:

    def __init__(self, total_vertices):
        self.total_vertices = total_vertices

        # Create an empty adjacency matrix
        self.adjacency_matrix = [
            [0 for column in range(total_vertices)]
            for row in range(total_vertices)
        ]

    # Display the shortest distances from the source vertex
    def print_solution(self, distances, source_vertex):

        print("Vertex\tDistance from Source")

        for vertex in range(self.total_vertices):
            print(vertex, "\t", distances[vertex])

    # Find the unvisited vertex with the smallest distance
    def find_minimum_distance_vertex(
        self,
        distances,
        shortest_path_tree
    ):

        minimum_distance = sys.maxsize
        minimum_vertex = -1

        # Search for the unvisited vertex with the
        # smallest known distance
        for vertex in range(self.total_vertices):

            if (
                distances[vertex] < minimum_distance
                and shortest_path_tree[vertex] == False
            ):
                minimum_distance = distances[vertex]
                minimum_vertex = vertex

        return minimum_vertex

    # Dijkstra's shortest path algorithm
    def dijkstra(self, source_vertex):

        # Initially, all distances are infinity
        distances = [sys.maxsize] * self.total_vertices

        # Distance from source to itself is 0
        distances[source_vertex] = 0

        # Keep track of vertices included in shortest path tree
        shortest_path_tree = [False] * self.total_vertices

        # Process all vertices
        for _ in range(self.total_vertices):

            current_vertex = self.find_minimum_distance_vertex(
                distances,
                shortest_path_tree
            )

            # Stop if no reachable unvisited vertex remains
            if current_vertex == -1:
                break

            # Mark the current vertex as processed
            shortest_path_tree[current_vertex] = True

            # Update distances of neighboring vertices
            for neighbor_vertex in range(self.total_vertices):

                if (
                    self.adjacency_matrix[current_vertex][neighbor_vertex] > 0
                    and shortest_path_tree[neighbor_vertex] == False
                    and distances[neighbor_vertex]
                    > distances[current_vertex]
                    + self.adjacency_matrix[current_vertex][neighbor_vertex]
                ):
                    distances[neighbor_vertex] = (
                        distances[current_vertex]
                        + self.adjacency_matrix[current_vertex][neighbor_vertex]
                    )

        # Display the shortest distances
        self.print_solution(distances, source_vertex)


# Driver code
if __name__ == "__main__":

    # Create a graph with 9 vertices
    my_graph = Graph(9)

    # Adjacency matrix
    my_graph.adjacency_matrix = [
        [0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
    ]

    # Find shortest paths from vertex 0
    my_graph.dijkstra(0)