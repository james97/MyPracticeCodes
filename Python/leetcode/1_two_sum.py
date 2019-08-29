"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    num_index = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement not in num_index.keys():
            num_index[complement] = index
        else:
            return [num_index[complement], index]

if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15, 7], 14) == [1, 4], f"wrong result"
