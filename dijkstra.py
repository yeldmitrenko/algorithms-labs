from queue import PriorityQueue

INFINITE = float('inf')


class Graph:
    def __init__(self, vertices_number):
        self.vertices = vertices_number
        self.edges = [[-1 for row in range(vertices_number)]
                      for column in range(vertices_number)]
        self.visited = []

    def add_edge(self, from_node_to_u, from_node_to_v, weight):
        self.edges[from_node_to_u][from_node_to_v] = weight
        self.edges[from_node_to_v][from_node_to_u] = weight

    def dijkstra(self, start_vertex):
        graph = {vertex: INFINITE for vertex in range(self.vertices)}
        graph[start_vertex] = 0

        queue = PriorityQueue()
        queue.put((0, start_vertex))

        while not queue.empty():
            (distance, current_vertex) = queue.get()
            self.visited.append(current_vertex)
            for neighbor in range(self.vertices):
                if self.edges[current_vertex][neighbor] != -1:
                    distance = self.edges[current_vertex][neighbor]
                    if neighbor not in self.visited:
                        old_cost = graph[neighbor]
                        new_cost = graph[current_vertex] + distance
                        if new_cost < old_cost:
                            queue.put((new_cost, neighbor))
                            graph[neighbor] = new_cost
        return graph


if __name__ == '__main__':
    graph = Graph(8)
    graph.add_edge(0, 3, 8)
    graph.add_edge(1, 4, 9)
    graph.add_edge(4, 2, 4)
    graph.add_edge(5, 0, 9)
    graph.add_edge(5, 4, 6)
    graph.add_edge(5, 1, 7)
    graph.add_edge(1, 2, 1)
    graph.add_edge(3, 1, 0)

    D = graph.dijkstra(1)

    for vertex in range(len(D)):
        print("Distance from 1 to vertex", vertex, "is", D[vertex])
