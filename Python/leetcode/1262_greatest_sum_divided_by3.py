"""
Given an array nums of integers, we need to find the maximum possible sum of elements of the array such that it is divisible by three.
"""
import itertools
from collections import defaultdict
from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        if len(nums) == 1:
            if nums[0] % 3 == 0:
                return nums[0]
            else:
                return 0
        mod_map = defaultdict(list)
        for num in nums:
            mod_map[num%3].append(num)
        max_value = sum(nums)
        mod_1 = sorted(mod_map[1], reverse=True)
        mod_2 = sorted(mod_map[2], reverse=True)
        if max_value != 0:
            if max_value % 3 == 1:
                if len(mod_1) >= 1:
                    if len(mod_2) <= 2:
                        max_value = max_value - mod_1[-1]
                    else:
                        max_value = max_value - min(mod_1[-1], mod_2[-1] + mod_2[-2])
                elif len(mod_2) >=2:
                    max_value = max_value - mod_2[-1] - mod_2[-2]
                else:
                    max_value = 0
            elif max_value % 3 == 2:
                if len(mod_2) >= 1:
                    if len(mod_1) <= 2:
                        max_value = max_value - mod_2[-1]
                    else:
                        max_value = max_value - min(mod_2[-1], mod_1[-1] + mod_1[-2])
                elif len(mod_1) >=2:
                    max_value = max_value - mod_1[-1] - mod_1[-2]
                else:
                    max_value = 0
        return max_value


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSumDivThree(nums = [2,6,2,2,7]))