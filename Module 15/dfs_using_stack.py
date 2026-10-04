def depth_first_search(graph_data, start_vertex):
    """
    Performs a depth-first search using a stack.

    Args:
        graph_data: The graph to search.
        start_vertex: The vertex where the search begins.

    Returns:
        A set containing all visited vertices.
    """

    visited_vertices = set()
    vertex_stack = [start_vertex]

    while vertex_stack:

        current_vertex = vertex_stack.pop()

        if current_vertex not in visited_vertices:

            visited_vertices.add(current_vertex)

            # Add neighboring vertices to the stack
            for neighbor_vertex in graph_data[current_vertex]:
                vertex_stack.append(neighbor_vertex)

    return visited_vertices


# Example graph
graph_data = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": [],
    "E": []
}


# Perform DFS starting from vertex A
visited_vertices = depth_first_search(graph_data, "A")

print(visited_vertices)
