#########################################################################
# File Name: bulb_switcher.py
# Author: Jun M
# mail: warrior97@gmail.com
# Created Time: Mon 21 Mar 14:06:23 2016
#Description: There are n bulbs that are initially off. You first turn on all the bulbs. Then, you turn off every second bulb. On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb. Find how many bulbs are on after n rounds.
#Level: Meduim
#########################################################################
#!/usr/bin/env python

class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        Solution: Only square number lights will be on, because its factor
        number is odd. For example, 4->1,2,4. 
        """
        if not n:
            return 0
        else:
            i = 1
            while ((i+1)**2) <= n:
                i += 1
            return i
