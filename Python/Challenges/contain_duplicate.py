#########################################################################
# File Name: contain_duplicate.py
# Author: Jun M
# mail: warrior97@gmail.com
# Created Time: Thu 17 Mar 15:55:10 2016
#########################################################################
#!/usr/bin/env python
import random

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        hint: Use a set or Dict
        """
        if not nums:
            return False
        else:
            nums_dict = {}
            for num in nums:
                if not num in nums_dict:
                    nums_dict[num] = 1
                else:
                    return True
            
            return False

if __name__ == "__main__":
    sol = Solution()
    test_case = [random.random(0,5000) for x in xrange(1000)]
    if sol.containsDuplicate(test_case):
        print "there are duplicated elements"
    else:
        print "there are not duplicate elements"
