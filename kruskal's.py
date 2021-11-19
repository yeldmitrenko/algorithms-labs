from typing import List


class Edge:
    def __init__(self, start_vertex, end_vertex, weight):
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex
        self.weight = weight


class Graph:
    def __init__(self, nodes_number):
        self.nodes_number = nodes_number
        self.edge_list = List[Edge]
        self.mst = []
        self.rank = 0
        self.parent = self

    def add(self, listkk: list[Edge]):
        self.edge_list = listkk

    def find_root(self):
        if self.parent is not self:
            self.parent = self.parent.find_root()
        return self.parent

    def union_sets(self, other):
        first_set_root = self.find_root()
        second_set_root = other.find_root()
        if first_set_root is second_set_root:
            return
        if first_set_root.rank < second_set_root.rank:
            first_set_root.parent = second_set_root
        elif first_set_root.rank > second_set_root.rank:
            second_set_root.parent = first_set_root
        else:
            second_set_root.parent = first_set_root
            first_set_root.rank += 1

    def kruskal_mst(self):
        nodes_not_unique = []
        for edge in sorted(self.edge_list, key=lambda Edge: Edge.weight):
            nodes_not_unique.append(edge.start_vertex)
            nodes_not_unique.append(edge.end_vertex)

        nodes = list(set(nodes_not_unique))

        result = dict((node, Graph(node)) for node in nodes)
        print(result)
        for edge in sorted(self.edge_list, key=lambda Edge: Edge.weight):

            start = result[edge.start_vertex].find_root()
            end = result[edge.end_vertex].find_root()

            if start is not end:
                self.mst.append(edge)
                start.union_sets(end)


if __name__ == '__main__':
    nodes_number = 7
    e1 = Edge(1, 2, 7)
    e2 = Edge(1, 4, 5)
    e3 = Edge(3, 5, 5)
    e4 = Edge(2, 5, 7)
    e5 = Edge(5, 7, 9)
    e6 = Edge(4, 6, 6)

    graph = Graph(nodes_number)
    graph.add([e1, e2, e3, e4, e5, e6])
    graph.kruskal_mst()

    print("\nEdges of minimum spanning tree in graph :", end=' ')
    cost = 0
    for edge in graph.mst:
        print("[" + str(edge.start_vertex) + "-" + str(edge.end_vertex) + "](" + str(edge.weight) + ")", end=' ')
        cost += edge.weight
    print("\nCost of minimum spanning tree : " + str(cost))
