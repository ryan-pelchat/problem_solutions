"""
Problem Title: 334. Increasing Triplet Subsequence
Platform: Leetcode
Problem URL: https://leetcode.com/problems/increasing-triplet-subsequence?envType=study-plan-v2&envId=leetcode-75
Difficulty: Medium
Categories: Array, Greedy

Author: Ryan Pelchat
Date Solved: 2025-08-20
Language: Python3

Problem Summary:
    Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

    Example 1:

    Input: nums = [1,2,3,4,5]
    Output: true
    Explanation: Any triplet where i < j < k is valid.

    Example 2:

    Input: nums = [5,4,3,2,1]
    Output: false
    Explanation: No triplet exists.

    Example 3:

    Input: nums = [2,1,5,0,4,6]
    Output: true
    Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.



    Constraints:

        1 <= nums.length <= 5 * 105
        -231 <= nums[i] <= 231 - 1


    Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?

Approach:
    - strategy
        - Keep 2 sets, 1st is all start of smallest values, 2nd is all possible second values
        - Loop through nums, add to first set
            - loop through 1st set, if current num bigger then promote to second set
            - loop through 2nd set,
                - if current num smaller, then demote to first list
                - if current num bigger, then we have 3 in a row stop calculating and return True
    - technique (two pointers, recursion, BFS, etc...)
        - This is exhaustive, and the time complexity reflects it

Time Complexity: 0(N^2)
Space Complexity: 0(N)

Notes:
    - There is a way to make this O(N) instead of O(N^2), I have to revisit this problem
"""

from typing import *


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # loop through values
        # 2 sets,
        # 1st are values encountered that is smaller than second list
        # 2nd are values encountered that is larger than first list

        ls1 = set()
        ls1.add(nums[0])
        ls2 = set()
        for num in nums:
            ls1.add(num)
            for val in ls1:
                if num > val:
                    ls2.add(num)
                    break
            for val in ls2:
                if num < val:
                    ls1.add(num)
                elif num > val:
                    return True
        return False
