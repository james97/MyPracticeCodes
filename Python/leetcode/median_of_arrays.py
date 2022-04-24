# Question: Find the median of two sorted arrays
from typing import List


def get_median_of_arrays(nums1: List[int], nums2: List[int]) -> float:
    c = nums1 + nums2
    c = quick_sort(c)
    if len(c) % 2 == 0:
        return (c[len(c)/2 - 1] + c[len(c)/2])/2
    else:
        return c[int(len(c)/2)]

def quick_sort(nums: List[int]):
    if len(nums) == 1 or not nums:
        return nums

    pivot_index = int(len(nums) / 2)
    pivot = nums[pivot_index]
    
if __name__ == "__main__":
    nums1 = [1, 3]
    nums2 = [2]
    assert get_median_of_arrays(nums1, nums2) == 2