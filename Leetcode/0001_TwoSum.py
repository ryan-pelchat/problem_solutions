"""
Problem Title: Two Sum
Platform: Leetcode
Problem URL: https://leetcode.com/problems/two-sum/description/
Difficulty: Easy
Category: ---

Author: Ryan Pelchat
Date Solved: May 8th 2025
Language: Python3

Problem Summary:
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.

Approach:
    - Double for loop check if they add up to target
    - In the second for loop you don't need to loop over half of the numbers because 1 + 2 is the same as 2 + 1

Time Complexity: 0(...)
    O(N^2)
Space Complexity: 0(...)
    O(N)

Notes:
    The timestamps are the amount of time I took to come up with that solution
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # 6:35
        for i, num in enumerate(nums):
            for i2, num2 in enumerate(nums[i:]):
                if (i != i2 + i) and (num + num2 == target):
                    return [i, i2 + i]

        # 4:57
        # for i, num in enumerate(nums):
        #     for i2, num2 in enumerate(nums):
        #         if (i != i2) and (num + num2 == target):
        #             return [i, i2]
