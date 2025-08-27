"""
Problem Title: Maximum Average Subarray I
Platform: Leetcode
Problem URL: https://leetcode.com/problems/maximum-average-subarray-i?envType=study-plan-v2&envId=leetcode-75
Difficulty: Easy
Categories: Array, Sliding Window

Author: Ryan Pelchat
Date Solved: 2025-08-27
Language: Python3

Problem Summary:
    You are given an integer array nums consisting of n elements, and an integer k.

    Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.



    Example 1:

    Input: nums = [1,12,-5,-6,50,3], k = 4
    Output: 12.75000
    Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

    Example 2:

    Input: nums = [5], k = 1
    Output: 5.00000



    Constraints:

        n == nums.length
        1 <= k <= n <= 105
        -104 <= nums[i] <= 104



Approach:
    - strategy
        - used a sliding window
        - since the quantity of averaged numbers is constant,
          you can instead find the largest sum instead of of largest avg
        - calculate sum, then subtract and add next numbers in window
        - slide window and return max sum found divided by k to get avg
    - technique (two pointers, recursion, BFS, etc...)
        - Sliding window
    - why did you choose it?
    - edge cases considered?

Time Complexity: 0(N)
Space Complexity: 0(1)

Notes:
"""

from typing import *


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # edge case, calculating avg or sum for every window is too demanding,
        # add and subtract the next and previous respectively to get the sum of the new window
        # then calculate the avg before returning for the largest window sum

        if k == len(nums):
            return sum(nums) / k

        currentSum = sum(nums[0:k])
        currentMax = currentSum

        for i in range(1, len(nums) - k + 1):
            currentSum = currentSum - nums[i - 1] + nums[i + k - 1]
            if currentMax < currentSum:
                currentMax = currentSum

        return currentMax / k
