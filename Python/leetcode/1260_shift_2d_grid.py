"""
Given a 2D grid of size n * m and an integer k. You need to shift the grid k times.

In one shift operation:

Element at grid[i][j] becomes at grid[i][j + 1].
Element at grid[i][m - 1] becomes at grid[i + 1][0].
Element at grid[n - 1][m - 1] becomes at grid[0][0].
Return the 2D grid after applying shift operation k times.
"""


import itertools
from typing import List

import numpy as np

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        if not grid:
            return grid
        np_array = np.array(grid)
        original_shape = np_array.shape
        grid = list(itertools.chain.from_iterable(grid))
        k = k % len(grid)
        grid = grid[k*-1:] + grid[:k * -1]
        array = np.reshape(np.array(grid), original_shape)
        return array.tolist()

if __name__ == "__main__":
    sol = Solution()
    print(sol.shiftGrid([[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], 4))