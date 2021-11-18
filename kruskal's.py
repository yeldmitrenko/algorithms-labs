from typing import List


class Edge:
    def __init__(self, start_vertex, end_vertex, weight):
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex
        self.weight = weight


class Graph:
    def __init__(self, nodes_number, edge_list: List[Edge]):
        self.nodes_number = nodes_number
        self.edge_list = edge_list
        self.mst = []

    def find_parent(self, parent, node):
        if node == parent[node]:
            return node
        return self.find_parent(parent, parent[node])

    def union_sets(self, parent, rank, first_set, second_set):
        first_set_root = self.find_parent(parent, first_set)
        second_set_root = self.find_parent(parent, second_set)
        if rank[first_set_root] < rank[second_set_root]:
            parent[first_set_root] = second_set_root
        elif rank[first_set_root] > rank[second_set_root]:
            parent[second_set_root] = first_set_root
        else:
            parent[second_set_root] = first_set_root
            rank[first_set_root] += 1

    def kruskal_mst(self):
        mst_index, sorted_edges_index = 0, 0
        parent = []
        rank = []

        self.edge_list = sorted(self.edge_list, key=lambda Edge: Edge.weight)
        for node in range(self.nodes_number):
            parent.append(node)
            rank.append(0)

        while mst_index < self.nodes_number - 1:
            start_vertex = self.edge_list[sorted_edges_index].start_vertex
            end_vertex = self.edge_list[sorted_edges_index].end_vertex
            weight = self.edge_list[sorted_edges_index].weight
            sorted_edges_index += 1
            edge = Edge(start_vertex, end_vertex, weight)
            start = self.find_parent(parent, start_vertex)
            end = self.find_parent(parent, end_vertex)
            if start != end:
                mst_index += 1
                self.mst.append(edge)
                self.union_sets(parent, rank, start, end)
        return self.mst


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

    graph = Graph(nodes_number, [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10])
    graph.kruskal_mst()

    print("\nEdges of minimum spanning tree in graph :", end=' ')
    cost = 0
    for edge in graph.mst:
        print("[" + str(edge.start_vertex) + "-" + str(edge.end_vertex) + "](" + str(edge.weight) + ")", end=' ')
        cost += edge.weight
    print("\nCost of minimum spanning tree : " + str(cost))
