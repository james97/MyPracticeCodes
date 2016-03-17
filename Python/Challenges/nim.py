#########################################################################
# File Name: nim.py
# Author: Jun M
# mail: warrior97@gmail.com
# Created Time: Thu 17 Mar 15:51:19 2016

#Description: You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

#Both of you are very clever and have optimal strategies for the game. Write a
#function to determine whether you can win the game given the number of stones in
#the heap.

#For example, if there are 4 stones in the heap, then you will never win the game: no matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend.

#Level: Easy
#########################################################################
#!/usr/bin/env python

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        If there are four stones, you always lose if you take stones first. Any other number less than 4 makes you win.
        If there are more than four, let's say 4n+m, m in (1,3), always take m stones and make sure the left amount is the multiple of 4. Then you can win
        """
        if not n:
            return False
        elif n % 4 == 0:
            return False
        else:
            return True
