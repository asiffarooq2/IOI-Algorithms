# Number of vertices in the graph
TOTAL_VERTICES = 4

# A large value representing infinity
# It means there is no direct path between two vertices
INFINITY = 99999


# Floyd-Warshall algorithm
# Finds the shortest distance between every pair of vertices
def floyd_warshall(adjacency_matrix):

    # Create a copy of the adjacency matrix
    # to store the shortest distances
    shortest_distances = [
        row[:] for row in adjacency_matrix
    ]

    # Consider each vertex as an intermediate vertex
    for intermediate_vertex in range(TOTAL_VERTICES):

        # Select the source vertex
        for source_vertex in range(TOTAL_VERTICES):

            # Select the destination vertex
            for destination_vertex in range(TOTAL_VERTICES):

                # Check whether going through the intermediate vertex
                # gives us a shorter path
                shortest_distances[source_vertex][destination_vertex] = min(
                    shortest_distances[source_vertex][destination_vertex],
                    shortest_distances[source_vertex][intermediate_vertex]
                    + shortest_distances[intermediate_vertex][destination_vertex]
                )

    # Display the shortest distance matrix
    display_shortest_distances(shortest_distances)


# Display the shortest distances between every pair of vertices
def display_shortest_distances(shortest_distances):

    print(
        "Shortest distances between every pair of vertices:"
    )

    for source_vertex in range(TOTAL_VERTICES):

        for destination_vertex in range(TOTAL_VERTICES):

            if (
                shortest_distances[source_vertex][destination_vertex]
                == INFINITY
            ):
                print("INF", end=" ")
            else:
                print(
                    "%7d"
                    % shortest_distances[source_vertex][destination_vertex],
                    end="  "
                )

        print()


# Driver code
if __name__ == "__main__":

    # Initial graph represented using an adjacency matrix
    adjacency_matrix = [
        [0, 5, INFINITY, 10],
        [INFINITY, 0, 3, INFINITY],
        [INFINITY, INFINITY, 0, 1],
        [INFINITY, INFINITY, INFINITY, 0]
    ]

    # Find shortest paths between all pairs of vertices
    floyd_warshall(adjacency_matrix)
