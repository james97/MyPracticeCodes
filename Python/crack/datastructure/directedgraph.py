#########################################################################
# File Name: directedgraph.py
# Author: Jun M
# mail: warrior97@gmail.com
#########################################################################

# !/usr/bin/env python
import os
import sys
from basicstructure import Vertex

class DirectedGraph(object):
    def __init__(self, graphmatrix):
        self.graphmatrix = graphmatrix
        self.vertexs = [Vertex(i) for i in xrange(len(graphmatrix))]
        self.graphlinks = self.build_linked_graph(graphmatrix)


    def build_linked_graph(self, graphmatrix):
        graphlinks = {}
        vertex_num = len(graphmatrix)
        for i in xrange(vertex_num):
            for j in xrange(vertex_num):
                #graphmatrix[i][j] is the weight of edge(i, j)
                if graphmatrix[i][j]:
                    if self.vertexs[i] in graphlinks.keys():
                        graphlinks[self.vertexs[i]].append((self.vertexs[j],
                                                       graphmatrix[i][j]))
                    else:
                        graphlinks[self.vertexs[i]] = []
                        graphlinks[self.vertexs[i]].append((self.vertexs[j], graphmatrix[i][j]))

        return graphlinks

    def search_vertex(self, num):
        for vertex in self.graphlinks.keys():
            if num == vertex.val:
                return vertex

        return None

    def breadth_first_search(self, num):
        for node in self.vertexs:
            node.pre =  None
            node.color = "white"
        vertex = self.search_vertex(num)
        if not vertex:
            return
        queue = []
        vertex.color = "white"
        vertex.distance = 0
        queue.append(vertex)
        while (len(queue)):
            node = queue.pop(0)
            if node.color == "white":
                node.color = "grey"
                if node in self.graphlinks.keys():
                    for edge in self.graphlinks[node]:
                        linked_vertex, weight = edge[0], edge[1]
                        linked_vertex.pre = node
                        linked_vertex.distance = node.distance + weight
                        queue.append(linked_vertex)
            if node.color == "grey":
                node.color = "black"
                print node

    def deep_frist_search(self):
        for node in self.vertexs:
            node.pre =  None
            node.color = "white"
        time = 0
        for node in self.vertexs:
            if node.color == "white":
                self.dfs_visit(node, time)

    def dfs_visit(self, node, time):
        time = time + 1
        node.distance = time
        node.color = "grey"
        if node in self.graphlinks.keys():
            for linked_node, weight in self.graphlinks[node]:
                if linked_node.color == "white":
                    linked_node.pre = node
                    self.dfs_visit(linked_node, time)

        node.color = "black"
        time = time + 1
        node.distance = time
        print node

    def dfs_stack(self):
        for node in self.vertexs:
            node.pre =  None
            node.color = "white"
        time = 0
        stack = []
        for node in self.vertexs:
            stack.append(node)
            time = 0
            while len(stack):
                node = stack.pop()
                if node.color == "white":
                    node.color = "grey"
                    stack.append(node)
                elif node.color == "grey":
                    node.color = "black"
                    print node
                if node in self.graphlinks.keys():
                    for child, _ in self.graphlinks[node]:
                        stack.append(child)


    def print_path(self, s, v):
        start = self.search_vertex(s)
        end = self.search_vertex(v)
        if not (start or end):
            return
        if (s == v):
            print s
            return
        if not end.pre:
            print "not path from s to v"
        else:
            print "{}<---".format(end),
            self.print_path(s, end.pre.val)




if __name__ == "__main__":
    graphmatrix = [[0 for i in xrange(9)] for j in xrange(9)]
    graphmatrix[0][1] = 9
    graphmatrix[0][2] = 3
    graphmatrix[2][3] = 3
    graphmatrix[3][1] = 2
    graphmatrix[3][4] = 4
    graphmatrix[3][6] = 2
    graphmatrix[4][5] = 8
    graphmatrix[4][8] = 3
    graphmatrix[6][7] = 10
    graphmatrix[8][7] = 2
    graph = DirectedGraph(graphmatrix)
    graph.deep_frist_search()
    print "\n"
    graph.dfs_stack()
    #graph.breadth_first_search(0)
    #graph.print_path(0,6)
