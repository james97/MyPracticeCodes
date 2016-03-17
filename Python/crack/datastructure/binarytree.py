#########################################################################
# File Name: binarytree.py
# Author: Jun M
# mail: warrior97@gmail.com
#########################################################################
#! /usr/bin/env python
from basicstructure import BinaryTreeNode
import random
from drawtree import drawtree


#TODO: refractor the class by removing codes using self.root. Try to
# add a parameter for the root of a tree

class Tree(object):
    def __init__(self):
        self.root = BinaryTreeNode()


class BinarySearchTree(Tree):
    def __init__(self):
        Tree.__init__(self)

    def __init__(self, numbers):
         self.build_BST(numbers)

    def search(self, num):
        node = self.root
        while (node.left or node.right):
            if (num < node.val) and node.left:
                node = node.left
            elif (num > node.val) and node.right:
                node = node.right
            elif (num == node.val):
                return True, node
            else:
                return False, node

        if (num == node.val):
            return True, node
        else:
            return False, node

    def tree_minimum(self, node):
        """return the minimum value in the tree whose root is node"""
        while node.left:
            node = node.left

        return node

    def tree_maximum(self, node):
        """return the maximum value in the tree whose root is node"""
        while node.right:
            node = node.right

        return node

    def tree_inorder_successor(self, num):
        """
        The successor of a node is either its minimum child in the
        right subtree or the first grandparent whose left child is
        the node's parent, not the right child. The idea is,
        because this is an inorder transpass. If a node has a right
        child, then the successor must be the minimum node in its
        left subtree. If not, the parent and the sibling tree of the
        node must be visited already, so we need to check its parent's
        parent until it is on the left branch of the grandparent. If
        its parent is still on the right branch of the grandparent,
        of course the grandparent has been visited already!
        """
        find, node = self.search(num)
        if find:
            if node.right:
                return self.tree_minimum(node.right)
            else:
                y = node.parent
                while y and node == y.right:
                    node = y
                    y = node.parent

                return y
        return None


    def tree_inorder_predecessor(self, num):
        """
        A reverse process of tree_inorder_successor()
        """
        find, node = self.search(num)
        if find:
            if node.left:
                return self.tree_maximum(node.left)
            else:
                y = node.parent
                while y and node == y.left:
                    node = y
                    y = node.parent
                return y

        return None

    def delete_direct_child(self, father, child):
        if father and father == child.parent:
            if father.left == child:
                father.left = None
            else:
                father.right = None

    def delete_node(self, num):
        find, node = self.search(num)
        if find:
            father = node.parent
            if not (node.left or node.right):
                self.delete_direct_child(father, node)
            elif not node.right:
                if father.left == node:
                    father.left = node.left
                    node.left.parent = father
                else:
                    father.right = node.left
                    node.left.parent = father
            elif not node.left:
                if father.left == node:
                    father.left = node.right
                    node.right.parent = father
                else:
                    father.right = node.right
                    node.right.parent = father

            elif node.right == self.tree_inorder_successor(node.val):
                """As the successor of node, node.right cannot have a left child"""
                if father.left == node:
                    father.left = node.right
                else:
                    father.right = node.right
                node.right.left = node.left
            else:
                y = self.tree_inorder_successor(node.val)
                print y
                y.parent.left = y.right
                node.val = y.val

    def build_BST(self, numbers):
        if not numbers:
            return
        self.root = BinaryTreeNode(numbers[0])
        for node_index in xrange(1, len(numbers)):
            self.insert_node(numbers[node_index])

    def random_build(self, node_amount):
        for x in xrange(node_amount):
            newval = random.randint(0,100)
            self.insert_node(newval)



    def insert_node(self, num):
        find, node = self.search(num)
        if not find:
            newnode = BinaryTreeNode(num)
            newnode.parent = node
            if num < node.val:
                node.left = newnode
            else:
                node.right = newnode

    def pre_order_trans(self, rootnode):
        if rootnode:
            print rootnode.val,
            self.pre_order_trans(rootnode.left)
            self.pre_order_trans(rootnode.right)

    def in_order_trans(self, rootnode):
        if rootnode:
            self.in_order_trans(rootnode.left)
            print rootnode.val,
            self.in_order_trans(rootnode.right)

    def post_order_trans(self, rootnode):
        if rootnode:
            self.post_order_trans(rootnode.left)
            self.post_order_trans(rootnode.right)
            print rootnode.val,

    def height(self, rootnode):
        if not rootnode:
            return 0
        else:
            return 1+ max(self.height(rootnode.left), self.height(rootnode.right))


if __name__ == "__main__":
    nums = [55, 30, 10, 5, 2, 20, 15, 25, 40, 35, 70, 60, 80, 75, 95]
    bst = BinarySearchTree(nums)
    #print "pre transpass"
    #bst.pre_order_trans(bst.root)
    print "\nin transpass"
    #bst.in_order_trans(bst.root)
    #print "\npost transpass"
    #bst.post_order_trans(bst.root)
    print "\n"
    drawtree.drawtree(bst.root)
    #print bst.tree_inorder_successor(35)
    #print bst.tree_inorder_predecessor(70)
    bst.delete_node(55)
    bst.delete_node(70)
    bst.delete_node(10)
    drawtree.drawtree(bst.root)

    #print bst.height(bst.root)