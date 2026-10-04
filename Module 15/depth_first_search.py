def depth_first_search(graph, start_vertex, visited_vertices=None):

    # Create an empty set during the first function call
    if visited_vertices is None:
        visited_vertices = set()

    # Visit the current vertex
    print(start_vertex, end=" ")
    visited_vertices.add(start_vertex)

    # Visit all neighboring vertices
    for neighbor_vertex in graph[start_vertex]:

        if neighbor_vertex not in visited_vertices:
            depth_first_search(
                graph,
                neighbor_vertex,
                visited_vertices
            )


# Example graph
graph_data = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}


print("DFS Traversal:")
depth_first_search(graph_data, "A")
