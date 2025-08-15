"""
Problem Title: Product of Array Except Self
Platform: Leetcode
Problem URL: https://leetcode.com/problems/product-of-array-except-self?envType=study-plan-v2&envId=leetcode-75
Difficulty: Medium
Categories: Array, Prefix Sum

Author: Ryan Pelchat
Date Solved:
Language: Python3

Problem Summary:
    Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

    You must write an algorithm that runs in O(n) time and without using the division operation.



    Example 1:

    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]

    Example 2:

    Input: nums = [-1,1,0,-3,3]
    Output: [0,0,9,0,0]

    Constraints:

        2 <= nums.length <= 105
        -30 <= nums[i] <= 30
        The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

    Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

Approach:
    - strategy
        - calculated forward prefix product notation and backward suffix product notation
            - ex. for [1, 2, 3, 4] prefix->[1, 2, 6, 24] and suffix->[24, 24, 12, 4]
        - Then at each index, took left prefix and multiplied with right suffix
            - ex. for index 1, do 1*12
        - This makes sense because left prefix has all product except at index, and ditto for suffix
    - edge cases considered
        - at start and end of list, there is no left prefix or right suffix
        - for start, use right suffix, for end, use left suffix


Time Complexity: 0(N)
Space Complexity: 0(N)

Notes:
"""

from typing import *


# import numpy as np
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forwardProd = nums[::]
        backwardProd = nums[::]
        outputLs = []

        # create the forward sums
        for i in range(1, len(nums)):
            forwardProd[i] = forwardProd[i] * forwardProd[i - 1]

        # create the backward sums
        for i in range(len(nums) - 2, -1, -1):
            backwardProd[i] = backwardProd[i] * backwardProd[i + 1]

        # create output list
        for i in range(len(nums)):
            if i == 0:
                outputLs.append(backwardProd[i + 1])
            elif i == len(nums) - 1:
                outputLs.append(forwardProd[i - 1])
            else:
                outputLs.append(forwardProd[i - 1] * backwardProd[i + 1])

        return outputLs
