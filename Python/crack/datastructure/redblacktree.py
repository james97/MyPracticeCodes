#########################################################################
# File Name: redblacktree.py
# Author: Jun M
# mail: warrior97@gmail.com
# check http://blog.csdn.net/v_july_v/article/details/6284050 for the
#  example
#########################################################################
#! /usr/bin/env python
from basicstructure import BinaryTreeNode
import random
from binarytree import BinarySearchTree
from drawtree import drawtree


class RedBlackTree(BinarySearchTree):
    nil = BinaryTreeNode(999, color="black")

    def __init__(self):
        super(RedBlackTree,self).__init__()
        self.root.parent = self.nil

    #Remember the way to call parent class's constructor
    #otherwise, self.root will not be accessible
    def __init__(self, numbers):
        self.build_RBT(numbers)
        self.point_to_nil(self.root)


    def left_rotate(self, node):
        if node.right == self.nil:
            return
        y = node.right
        node.right = y.left
        if y.left != self.nil:
            y.left.parent = node
        y.parent = node.parent
        if node.parent == self.nil:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y
        y.left = node
        node.parent = y

    def right_rotate(self, node):
        #If a node has a nil left, it can't be right_rotated
        if node.left == self.nil:
            return
        x = node.left
        node.left = x.right
        if x.right != self.nil:
            x.right.parent = node
        x.parent = node.parent
        if node.parent == self.nil:
            self.root = x
        elif node == node.parent.left:
            node.parent.left = x
        else:
            node.parent.right = x
        x.right = node
        node.parent = x



    def insert_node(self, num):
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if num < x.val:
                x = x.left
            else:
                x = x.right
        newnode = BinaryTreeNode(num)
        newnode.parent = y
        if y == self.nil:
            self.root = newnode
        elif newnode.val < y.val:
            y.left = newnode
        else:
            y.right = newnode

        newnode.left = self.nil
        newnode.right = self.nil
        newnode.color = "red"
        self.rb_insert_fixup(newnode)

    def rb_insert_fixup(self, node):
        while node.parent.color == "red":
            if node.parent == node.parent.parent.left:
                y = node.parent.parent.right
                if y.color == "red":
                    node.parent.color = "black"
                    y.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                elif node == node.parent.right:
                    node = node.parent
                    self.left_rotate(node)
                else:
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.right_rotate(node.parent.parent)
            else:
                y = node.parent.parent.left
                if y.color == "red":
                    node.parent.color = "black"
                    y.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                elif node == node.parent.left:
                    node = node.parent
                    self.right_rotate(node)
                else:
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.left_rotate(node.parent.parent)
            self.root.color = "black"

    def build_RBT(self, numbers):
        if not numbers:
            return
        self.root = BinaryTreeNode(numbers[0])
        self.root.parent = self.nil
        self.root.left = self.nil
        self.root.right = self.nil
        for node_index in xrange(1, len(numbers)):
            self.insert_node(numbers[node_index])
            drawtree.drawtree(self.root)

    def transplant(self, u, v):
        """
        replace the u subtree with the v subtree
        """
        if u.parent == self.nil:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def delete_node(self, num):
        find, z = self.search(num)
        if find:
            y = z
            y_original_color = y.color
            if z.left == self.nil and z.right == self.nil:
                if z == z.parent.left:
                    z.parent.left = self.nil
                else:
                    z.parent.right = self.nil
                return

            if z.left == self.nil:
                x = z.right
                self.transplant(z, x)
            elif z.right == self.nil:
                x = z.left
                self.transplant(z, x)
            else:
                y = self.tree_minimum(z.right)
                y_original_color = y.color
                x = y.right
                if y.parent == z:
                    x.parent = y
                else:
                    self.transplant(y, y.right)
                    y.right = z.right
                    y.right.parent = y
                self.transplant(z,y)
                y.left = z.left
                y.left.p = y
                y.color = z.color

            if y_original_color == "black":
                self.delete_fixup(x)

    def delete_fixup(self, x):
        while x != self.root and x.color == "black":
            if x == x.parent.left:
                w = x.parent.right
                if w.color == "red":
                    w.color = "black"
                    x.parent.color = "red"
                    self.left_rotate(x.parent)
                    w = x.parent.right

                if w.left.color == "black" and w.right.color == "black":
                    w.color = "red"
                    x = x.parent

                elif w.right.color == "black":
                    w.left.color == "black"
                    w.color = "red"
                    self.right_rotate(w)
                    w = x.parent.right

                w.color = x.parent.color
                x.parent.color = "black"
                w.right.color = "black"
                self.left_rotate(x.parent)
                x = self.root

            else:
                pass
            #TODO: to be continued




    def point_to_nil(self, node):
        if node and node != self.nil:
            self.point_to_nil(node.left)
            if not node.left:
                node.left = self.nil
            if not node.right:
                node.right = self.nil
            self.point_to_nil(node.right)


if __name__ == "__main__":
    #nums = [55, 30, 10, 5, 2, 20, 15, 25, 40, 35, 70, 60, 80, 75, 95]
    nums = [12, 1, 9, 2, 0, 11, 7, 19, 4, 15, 18, 5, 14, 13, 10, 16, 6,
3, 8, 17]
    rbt = RedBlackTree(nums)

    #print "pre transpass"
    #rbt.pre_order_trans(rbt.root)
    #print "\nin transpass"
    #rbt.in_order_trans(rbt.root)
    #print "\npost transpass"
    #rbt.post_order_trans(rbt.root)
    print "\n"
    drawtree.drawtree(rbt.root)
    #_, node = rbt.search(20)
    #rbt.left_rotate(node)
    #_, node = rbt.search(20)
    #rbt.right_rotate(node)
    #drawtree.drawtree(rbt.root)
    #print rbt.tree_inorder_successor(35)
    #print rbt.tree_inorder_predecessor(70)
    #rbt.delete(55)
    #rbt.delete(70)
    #rbt.delete(10)
    #drawtree.drawtree(rbt.root)

    #print rbt.height(rbt.root)