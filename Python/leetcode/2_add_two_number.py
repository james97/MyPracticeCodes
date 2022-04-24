"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        else:
            output_start = ListNode(-1)
            carry = 0
            current_node = output_start
            while l1.next and l2.next:
                sum = (l1.val + l2.val) % 10 + carry
                carry = (l1.val + l2.val) / 10
                new_node = ListNode(sum)
                current_node.next = new_node
                current_node = new_node



if __name__ == "__main__":
