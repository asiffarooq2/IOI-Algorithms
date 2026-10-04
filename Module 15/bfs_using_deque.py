from collections import deque


def breadth_first_search(graph, start_vertex):

    visited_vertices = set()
    vertex_queue = deque([start_vertex])

    visited_vertices.add(start_vertex)

    while vertex_queue:

        current_vertex = vertex_queue.popleft()

        print(current_vertex, end=" ")

        # Visit all neighboring vertices
        for neighbor_vertex in graph[current_vertex]:

            if neighbor_vertex not in visited_vertices:
                vertex_queue.append(neighbor_vertex)
                visited_vertices.add(neighbor_vertex)


# Example graph
graph_data = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}


print("BFS Traversal:")
breadth_first_search(graph_data, "A")
