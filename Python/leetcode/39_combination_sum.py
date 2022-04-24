"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if target <=0:
            return []
        if not candidates:
            return []
        if len(candidates) == 1:
            if target % candidates[0] == 0:
                return [candidates * (target / candidates[0])]
        else:
            pass




if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum([2,3,5], 9))
