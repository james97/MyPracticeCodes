#########################################################################
# File Name: undirectedgraph.py
# Author: Jun M
# mail: warrior97@gmail.com
#########################################################################

# !/usr/bin/env python
import os
import sys
from basicstructure import Vertex, Edge

class UndirectedGraph(object):
    def __init__(self):
        self.vertexes = []
        self.edges = []

    def add_edge(self, edge):
        if not (edge.start in self.vertexes and edge.end in
            self.vertexes):
            raise ValueError("not both vertexes of edge {} are in the graph".format(edge))
        else:
            for exist_edge in self.edges:
                if (exist_edge.start, exist_edge.end) == (edge.start,
                                                          edge.end) or (exist_edge.start, exist_edge.end) == (edge.end,
                                                          edge.start):
                    return

            self.edges.append(edge)

    def add_vertex(self, vertex):
        for exist_vertex in self.vertexes:
            if vertex.val == exist_vertex.val:
                return

        self.vertexes.append(vertex)

    def remove_vertex(self, vertex):
        pos = self.vertexes.index(vertex)
        if pos:
            del self.vertexes[pos]

        for edge in self.edges:
            if edge.start == vertex or edge.end == vertex:
                self.edges.remove(vertex)

    def remove_edge(self, edge):
        pos = self.edges.index(edge)
        if pos:
            del self.edges[pos]

    def mst_prim(self):
        unvisited = set(self.vertexes)
        tmp_edges = list(self.edges)
        visited = set([])
        mst = []
        visited.add(self.vertexes[0])
        unvisited.remove(self.vertexes[0])
        shortest_edge = None

        while len(unvisited) >0 :
            shortest_edge = None
            min_distance = 99999
            for node in visited:
                for edge in tmp_edges:
                    if self.prim_edge_select(edge, visited):
                        if edge.weight < min_distance:
                            min_distance = edge.weight
                            shortest_edge = edge
            if shortest_edge:
                visited.add(shortest_edge.start)
                visited.add(shortest_edge.end)
                if shortest_edge.start in unvisited:
                    unvisited.remove(shortest_edge.start)
                else:
                    unvisited.remove(shortest_edge.end)
                tmp_edges.remove(shortest_edge)
                mst.append(shortest_edge)

        return mst

    def prim_edge_select(self, edge, visited):
        if edge.start in visited and edge.end in visited:
            return False
        elif not (edge.start in visited or edge.end in visited):
            return False
        else:
            return True

    def mst_kruskal(self):
        unvisited = set(self.vertexes)
        belong_set = {}
        for vertex in unvisited:
            assert isinstance(vertex, object)
            belong_set[vertex] = {vertex}
        tmp_edges = sorted(self.edges, key=lambda edge:edge.weight)
        mst = []
        for edge in tmp_edges:
            if belong_set[edge.start] != belong_set[edge.end]:
                combine_set = belong_set[edge.start].union(belong_set[edge.end])
                #Remember to update the set for each node in
                #  the combined_set. This is not mentioned
                #  in Introduction to Algorithms
                for node in combine_set:
                    belong_set[node] = combine_set
                mst.append(edge)
                print "add edge  {} {} {}".format(edge.start.val, edge.end.val, edge.weight)

        return mst

    def dijkstra(self, s):
        for vertex in self.vertexes:
            vertex.distance = 99999
            vertex.pre = None

        s.distance = 0
        curr_nearest = s
        unvisited = set(self.vertexes)
        unvisited.remove(s)
        while len(unvisited):
            curr_nearest_edge = [edge for edge in self.edges if edge.start == curr_nearest or edge.end == curr_nearest]
            for edge in curr_nearest_edge:
                if edge.start == curr_nearest:
                    other_side = edge.end
                else:
                    other_side = edge.start
                if other_side.distance > curr_nearest.distance + edge.weight:
                    other_side.distance = curr_nearest.distance + edge.weight
                    other_side.pre = curr_nearest

            min_dis = 99999
            for vertex in unvisited:
                if vertex.distance < min_dis:
                    min_dis = vertex.distance
                    curr_nearest = vertex

            unvisited.remove(curr_nearest)

        print "\n"
        for vertex in self.vertexes:
            print vertex


if __name__ == "__main__":
    undirect = UndirectedGraph()
    vertexs = Vertex.create_vertex_list(["A", "B", "C", "D", "E",
                                         "F", "G", "H"])
    for vertex in vertexs:
        undirect.add_vertex(vertex)
    undirect.add_edge(Edge(vertexs[0], vertexs[1], 8))
    undirect.add_edge(Edge(vertexs[0], vertexs[2], 2))
    undirect.add_edge(Edge(vertexs[0], vertexs[3], 5))
    undirect.add_edge(Edge(vertexs[1], vertexs[3], 2))
    undirect.add_edge(Edge(vertexs[1], vertexs[5], 13))
    undirect.add_edge(Edge(vertexs[2], vertexs[3], 2))
    undirect.add_edge(Edge(vertexs[2], vertexs[4], 5))
    undirect.add_edge(Edge(vertexs[3], vertexs[4], 1))
    undirect.add_edge(Edge(vertexs[3], vertexs[5], 6))
    undirect.add_edge(Edge(vertexs[3], vertexs[6], 8))
    undirect.add_edge(Edge(vertexs[4], vertexs[6], 1))
    undirect.add_edge(Edge(vertexs[5], vertexs[6], 2))
    undirect.add_edge(Edge(vertexs[5], vertexs[7], 3))
    undirect.add_edge(Edge(vertexs[6], vertexs[7], 6))

    print "prim mst:\n"
    for edge in undirect.mst_prim():
        print edge
    print "kruskal mst:\n"
    for edge in undirect.mst_kruskal():
        print edge

    print "Dijkstra start from {}\n".format(vertexs[0])
    print undirect.dijkstra(vertexs[0])
