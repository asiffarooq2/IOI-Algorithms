from collections import defaultdict


class Graph:

    def __init__(self):
        self.adjacency_list = defaultdict(list)

    def add_edge(self, source, destination):
        self.adjacency_list[source].append(destination)

    def breadth_first_search(self, start_vertex):

        visited = [False] * (max(self.adjacency_list) + 1)
        queue = []

        # Add the starting vertex to the queue
        queue.append(start_vertex)
        visited[start_vertex] = True

        # Continue until the queue is empty
        while queue:

            current_vertex = queue.pop(0)

            print(current_vertex, end=" ")

            # Visit all neighboring vertices
            for neighbor_vertex in self.adjacency_list[current_vertex]:

                if not visited[neighbor_vertex]:
                    queue.append(neighbor_vertex)
                    visited[neighbor_vertex] = True


# Test the BFS algorithm
if __name__ == "__main__":

    my_graph = Graph()

    # Add edges to the graph
    my_graph.add_edge(0, 1)
    my_graph.add_edge(0, 2)
    my_graph.add_edge(1, 2)
    my_graph.add_edge(2, 0)
    my_graph.add_edge(2, 3)
    my_graph.add_edge(3, 3)

    print("BFS traversal starting from vertex 2:")

    my_graph.breadth_first_search(2)
