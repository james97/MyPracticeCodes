#########################################################################
# File Name: basicstructure.py
# Author: Jun M
# mail: warrior97@gmail.com
#########################################################################

# !/usr/bin/env python
class BinaryTreeNode(object):
    def __init__(self, val=0, left=None, right=None, parent=None,
                 color=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        self.color = color


    def __str__(self):
        if self.color:
            return self.color + str(self.val)
        else:
            return str(self.val)


class Linkednode(object):
    def __init__(self, val, next_node=None):
        self.val = val
        self.next_node = next_node


class MaxHeap(object):

    def __init__(self, nums=[]):
        self.nums = nums


    def max_heapify(self, end, node_index):
        """
        In a max heap, the root node is the largest element in the list,
        and a heap is a complete binary tree, so it can be stored in a
        list. The left and right children of node i is i*2 and i*2+1
        :param node_index: max_heapify the heap whose root is nums[i]
        """
        left = node_index * 2 + 1
        right = node_index * 2 + 2

        largest = node_index
        if left < end and (self.nums[node_index] < self.nums[
            left]):
            largest = left

        if right < end and (self.nums[right] > self.nums[
            largest]):
            largest = right

        if largest != node_index:
            self.nums[largest], self.nums[node_index] = self.nums[
                                                            node_index], self.nums[largest]
            self.max_heapify(end, largest)


    def build_max_heap(self):
        for i in xrange(len(self.nums)/2 - 1, -1, -1):
            self.max_heapify(len(self.nums), i)


    def heap_sort(self):
        """
        Failed initially because I use nums[:i] instead of num itself
        with a boundary end i. The problem is that Python will make
        a copy of nums[:i] instead of modify it directly. So each time
        I call max_heapify(nums[:i]), the actual nums will not be
        changed. Be careful of changing a list through functions.
        When calling build_max_heap, each node should be the maximum
        in its heap. So the maximum of node[1] and node[2] must
        be the largest one of the next round, and it will recursively
        use max_heapify to maintain the rule of its subheaps, so we
        do not need to call build_max_heap again
        """
        length = len(self.nums)
        self.build_max_heap()
        for i in xrange(length-1, 0, -1):
            self.nums[0], self.nums[i] = self.nums[i], self.nums[0]
            self.max_heapify(i, 0)


class Vertex(object):
    def __init__(self, val, color="white", distance=99999, pre=None,
                 timestamp=0):
        self.val = val
        self.color = color
        self.pre = pre
        self.distance = distance
        self.timestamp = timestamp

    #Way to create a static method, no "self" needed in the argument
    # list
    @staticmethod
    def create_vertex_list(names):
        rtype = [Vertex(name) for name in names]
        return rtype

    def __str__(self):
        return "val:{} col:{} dis:{}".format(str(self.val), self.color,
                                  self.distance)


class Edge(object):
    def __init__(self, start, end, weight=1):
        self.start = start
        self.end = end
        self.weight = weight

    def __str__(self):
        return "<{},{}>({})".format(self.start, self.end, self.weight)