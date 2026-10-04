# Add an edge to an undirected graph
def add_edge(adjacency_list, vertex1, vertex2):
    adjacency_list[vertex1].append(vertex2)
    adjacency_list[vertex2].append(vertex1)


# Perform DFS recursively from a given vertex
def depth_first_search(current_vertex, adjacency_list, visited_vertices):

    visited_vertices[current_vertex] = True

    for neighbor_vertex in adjacency_list[current_vertex]:

        if not visited_vertices[neighbor_vertex]:
            depth_first_search(
                neighbor_vertex,
                adjacency_list,
                visited_vertices
            )


# Count the number of connected components in the graph
def count_connected_components(adjacency_list, total_vertices):

    visited_vertices = [False] * total_vertices
    component_count = 0

    for vertex in range(total_vertices):

        # If the vertex has not been visited,
        # it belongs to a new connected component
        if not visited_vertices[vertex]:

            depth_first_search(
                vertex,
                adjacency_list,
                visited_vertices
            )

            component_count += 1

    return component_count


# Driver code
if __name__ == "__main__":

    # Total number of vertices
    total_vertices = 5

    # Create an empty adjacency list
    adjacency_list = [
        [] for vertex in range(total_vertices)
    ]

    # Add edges
    add_edge(adjacency_list, 0, 1)
    add_edge(adjacency_list, 0, 2)
    add_edge(adjacency_list, 0, 3)
    add_edge(adjacency_list, 3, 4)

    # Count and display connected components
    print(
        "Number of connected components:",
        count_connected_components(
            adjacency_list,
            total_vertices
        )
    )
