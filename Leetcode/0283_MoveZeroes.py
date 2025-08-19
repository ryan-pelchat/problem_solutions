"""
Problem Title: 283. Move Zeroes
Platform: Leetcode
Problem URL: https://leetcode.com/problems/move-zeroes?envType=study-plan-v2&envId=leetcode-75
Difficulty: East
Categories: Array, Two Pointers

Author: Ryan Pelchat
Date Solved:
Language: Python3

Problem Summary:
    Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

    Note that you must do this in-place without making a copy of the array.



    Example 1:

    Input: nums = [0,1,0,3,12]
    Output: [1,3,12,0,0]

    Example 2:

    Input: nums = [0]
    Output: [0]



    Constraints:

        1 <= nums.length <= 104
        -231 <= nums[i] <= 231 - 1


    Follow up: Could you minimize the total number of operations done?

Approach:
    - strategy
        - You only need to look at every number once
        - Indexed through list popping and appending zeroes
        - If a zero is found, the index does't increment but the operation count does
            - this is because if you pop, the values in list shift down
            - operations increment because you need to make sure you only see every value once
        - once operation count or index reaches the size the of the list then we are finished

Time Complexity: 0(N)
    - O(N) if not counting the shift of indexes in pop() method, otherwise O(N^2)
    - O(N^2) in worst case, for example, in a list of all 0s
Space Complexity: 0(...)
    - O(1), it modifies the list in place

Notes:
"""

from typing import *


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        numOperations = 0
        while i < len(nums) and numOperations < len(nums):
            if nums[i] == 0:
                nums.append(nums.pop(i))
                numOperations += 1
            else:
                i += 1
                numOperations += 1
