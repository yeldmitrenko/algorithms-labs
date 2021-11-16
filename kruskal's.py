from typing import List


class Edge:
    def __init__(self, start_vertex, end_vertex, weight):
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex
        self.weight = weight


class Graph:
    def __init__(self, nodes_number, edge_list : List[Edge]):
        self.nodes_number = nodes_number
        self.edge_list = edge_list
        self.parent = []
        self.rank = []
        self.mst = []

    def find_parent(self, node):
        if node == self.parent[node]:
            return node
        return self.find_parent(self.parent[node])

    def kruskal_mst(self):
        self.edge_list.sort(key=lambda Edge : Edge.weight)
        self.parent = [None] * self.nodes_number
        self.rank = [None] * self.nodes_number

        for node in range(self.nodes_number):
            self.parent[node] = node
            self.rank[node] = 0

        for edge in self.edge_list:
            root1 = self.find_parent(edge.start_vertex)
            root2 = self.find_parent(edge.end_vertex)
            if root1 != root2:
                self.mst.append(edge)
                if self.rank[root1] < self.rank[root2]:
                    self.parent[root1] = root2
                    self.rank[root2] += 1
                else:
                    self.parent[root2] = root1
                    self.rank[root1] += 1
        print("\nEdges of minimum spanning tree in graph :", end=' ')
        cost = 0
        for edge in self.mst:
            print("[" + str(edge.start_vertex) + "-" + str(edge.end_vertex) + "](" + str(edge.weight) + ")", end=' ')
            cost += edge.weight
        print("\nCost of minimum spanning tree : " + str(cost))


if __name__ == '__main__':
    nodes_number = 6
    e1 = Edge(0, 1, 4)
    e2 = Edge(0, 2, 1)
    e3 = Edge(0, 3, 5)
    e4 = Edge(1, 3, 2)
    e5 = Edge(1, 4, 3)
    e6 = Edge(1, 5, 3)
    e7 = Edge(2, 3, 2)
    e8 = Edge(2, 4, 8)
    e9 = Edge(3, 4, 1)
    e10 = Edge(4, 5, 3)

    graph1 = Graph(nodes_number, [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10])
    graph1.kruskal_mst()

    num_nodes = 7
    a = Edge(0, 1, 1)
    b = Edge(0, 2, 2)
    c = Edge(0, 3, 1)
    d = Edge(0, 4, 1)
    e = Edge(0, 5, 2)
    f = Edge(0, 6, 1)
    g = Edge(1, 2, 2)
    h = Edge(1, 6, 2)
    i = Edge(2, 3, 1)
    j = Edge(3, 4, 2)
    k = Edge(4, 5, 2)
    l = Edge(5, 6, 1)

    graph2 = Graph(num_nodes, [a, b, c, d, e, f, g, h, i, j, k, l])
    graph2.kruskal_mst()
