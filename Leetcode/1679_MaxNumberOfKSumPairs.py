"""
Problem Title: 1679. Max Number of K-Sum Pairs
Platform: Leetcode
Problem URL: https://leetcode.com/problems/max-number-of-k-sum-pairs?envType=study-plan-v2&envId=leetcode-75
Difficulty: Medium
Categories: Array, Hash Table, Two, Pointers, Sorting, Weekly Contest 218

Author: Ryan Pelchat
Date Solved: 2025-08-23
Language: Python3

Problem Summary:
    You are given an integer array nums and an integer k.

    In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

    Return the maximum number of operations you can perform on the array.



    Example 1:

    Input: nums = [1,2,3,4], k = 5
    Output: 2
    Explanation: Starting with nums = [1,2,3,4]:
    - Remove numbers 1 and 4, then nums = [2,3]
    - Remove numbers 2 and 3, then nums = []
    There are no more pairs that sum up to 5, hence a total of 2 operations.

    Example 2:

    Input: nums = [3,1,3,4,3], k = 6
    Output: 1
    Explanation: Starting with nums = [3,1,3,4,3]:
    - Remove the first two 3's, then nums = [1,4,3]
    There are no more pairs that sum up to 6, hence a total of 1 operation.



    Constraints:

        1 <= nums.length <= 105
        1 <= nums[i] <= 109
        1 <= k <= 109



Approach:
    - strategy
        - 2 pointers
        - sort the list
        - if sum of pointers too large pt1+=1
        - if sum of pointers too small pt2-=1
        - if sum of pointers perfect, pt1+=1, pt2-=1
    - technique (two pointers, recursion, BFS, etc...)
        - 2 pointers
    - edge cases considered?
        - The list needs to be sorted,
            - ex: [4,1,3,2,2] ans is 1, no sorting it is 0

Time Complexity: 0(NlogN)
    - This is because the best sorting algorithm is NlogN
Space Complexity: 0(1)

Notes:
"""

from typing import *


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # 2 pointers, pt1, pt2
        # pt1 at start and pt2 at end of nums
        # sort list
        # increment pt1 if nums[pt1] + nums[pt2] < k
        # decrecemt pt2 if nums[pt1] + nums[pt2] > k
        # increment and decrement both if nums[pt1] + nums[pt2] == k
        # needs to be sorted:
        # ex: [4,1,3,2,2] ans is 1, no sorting it is 0
        nums.sort()
        pt1 = 0
        pt2 = len(nums) - 1
        count = 0

        while pt1 < pt2:
            if nums[pt1] + nums[pt2] < k:
                pt1 += 1
            elif nums[pt1] + nums[pt2] > k:
                pt2 -= 1
            else:
                pt1 += 1
                pt2 -= 1
                count += 1
        return count
