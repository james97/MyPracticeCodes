# !usr/bin/env python
import os
import random
import math
from basicstructure import MaxHeap

"""
Implement regular sorting methods and practise my programming style
"""

#In memory sort


def descending(a, b):
    return a >= b


def ascending(a, b):
    return a <= b


def insert_sort(nums, order=ascending):
    """
    2(n-1) movements, n-1 comparisons, worse O(n^2), suitable for
    conditions that most numbers are ordered and the sequence is short
    """
    if not nums:
        return

    for i in xrange(1, len(nums)):
        j = 0
        while not order(nums[i], nums[j]):
            j += 1
        tmp = nums[i]
        for k in xrange(i, j, -1):
            nums[k] = nums[k - 1]
        nums[j] = tmp

    return nums


def shell_sort(nums, order=ascending):
    """
    shell sort is a kind of insert sort, unstable
    n-1 comparisons, worse O(n^2)
    Be careful of the boundary of elements for comparisons
    It's idea is sort the sublists contain elements whose gap is n,
    and then reduce n to 1
    """
    if not nums:
        return

    gap = len(nums) / 3
    while gap > 0:
        for i in xrange(gap, len(nums)):
            tmp = nums[i]
            j = i
            while j > 0:
                j -= gap
            while not order(nums[i], nums[j]):
                j += gap
            for k in xrange(i, j, gap*-1):
                nums[k] = nums[k - gap]
            nums[j] = tmp

        gap /= 2

    return nums


def select_sort(nums, order=ascending):
    """
    unstable
    O(n^2) comparisons, n-1 swaps, worse O(n^2)
    """
    if not nums:
        return

    for i in xrange(len(nums)):
        current_best = i
        for j in xrange(i, len(nums)):
            if order(nums[j], nums[current_best]):
                current_best = j
        nums[i], nums[current_best] = nums[current_best], nums[i]

    return nums


def quick_sort(nums, p, r, order=ascending):
    """
    Usually, this is the most efficient sorting method. Worst case
    O(n^2), average O(nlgn)
    """
    if not nums:
        return
    if p < r:
        pivot = partition(nums, p, r, order)
        quick_sort(nums, p, pivot-1, order)
        quick_sort(nums, pivot+1, r, order)


def partition(nums, p, r, order):
    if not nums:
        return
    x = nums[r]
    i = p - 1
    for j in xrange (p, r):
        if order(nums[j], x):
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i+1], nums[r] = nums[r], nums[i+1]
    return i+1


def merge_sort(nums, order=ascending):

    if len(nums) > 1:
        lefthalf = nums[:len(nums)/2]
        righthalf = nums[len(nums)/2:]

        merge_sort(lefthalf, order)
        merge_sort(righthalf, order)
        leftindex = 0
        rightindex = 0
        numsindex = 0
        while (leftindex < len(lefthalf)) and (rightindex < len(righthalf)):
            if order(lefthalf[leftindex], righthalf[rightindex]):
                nums[numsindex] = lefthalf[leftindex]
                leftindex += 1
                numsindex += 1
            else:
                nums[numsindex] = righthalf[rightindex]
                rightindex += 1
                numsindex += 1

        while (leftindex < len(lefthalf)):
            nums[numsindex] = lefthalf[leftindex]
            leftindex += 1
            numsindex += 1

        while (rightindex < len(righthalf)):
            nums[numsindex] = righthalf[rightindex]
            rightindex += 1
            numsindex += 1

#Linear time sort algorithms below: counting-sort, radix_sort,
# miss bucket sort which is good for numeric values in a uniform
# distribution. The basic idea is map numbers into different buckets
# and rank them in them. After ranking numbers in each bucket,
# while the buckets are in order already, the sort process is done.


def counting_sort(nums, k):
    """
    Assumption: all the n numbers are within [0,k). Use extra space to
    save time, so we have one list with length n and another with
    length k. The idea is that if there are m numbers smaller than x,
    then x should be
     at position m+1. We can put that in the right place directly.
     Sounds like the way to find a pivot for quick sort. let's suppose
     all elements are different first. This is a perfect way to deal
     with linear time sort. However, it is only useful for discrete
     elements like integers with a range.
    """
    B = [0 for x in xrange(len(nums))]
    C = [0 for x in xrange(k)]

    for num in nums:
        C[num] += 1

    for i in xrange(1, k):
        C[i] = C[i] + C[i-1]

    for j in xrange(len(nums)-1, -1, -1):
        #for j in xrange(len(nums) is also OK
        #and I think it is still stable because the ranks of the same
        #  number is ignored already
        B[C[nums[j]] -1] = nums[j]
        C[nums[j]] -= 1

    return B


def radix_sort(nums, radix=10):
    """
    Similar to the counting sort,but more suitable for words with the same length.
    So to summarize, in order to sort numbers or strings in a linear
    time, have to prepare a list and map numbers into each position.
    While the positions are naturally ranked alphabetically or
    numerically, we save time for ranking.
    """

    K = int(math.ceil(math.log(max(nums), radix)))
    bucket = [[] for i in range(radix)]
    for i in range(1, K+1):
        for val in nums:
            bucket[val%(radix**i)/(radix**(i-1))].append(val)
        del nums[:]
        for each in bucket:
            nums.extend(each)
        bucket = [[] for i in range(radix)]


if __name__ == "__main__":
    numbers = [random.randint(0, 100) for i in xrange(6)]
    #maxheap = MaxHeap(numbers)
    #maxheap.heap_sort()
    #print maxheap.nums
    #print select_sort(numbers)
    #print shell_sort(numbers, descending)
    #quick_sort(numbers, 0, len(numbers)-1)
    #print numbers
    #print counting_sort(numbers, 20)
    radix_sort(numbers)
    print numbers
    exit(0)

