from typing import *

"""
Problem Title: Binary Search
Platform: LeetCode
Problem URL: https://leetcode.com/problems/binary-search/description/
Difficulty: Easy
Categories: Array, Binary Search

Author: Ryan Pelchat
Date Solved: 2025-06-12
Language: Python3

Problem Summary:
    Given an array of integers nums which is sorted in ascending order, and an integer target,
    write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
    You must write an algorithm with O(log n) runtime complexity.

Approach:
    - a general binary search algorithm using 2 pointers

Time Complexity: 0(logN)
    - In the worst case possible, you half your solution space with every iteration
Space Complexity: 0(1)
    - The variables that are stored does not increase with the size of the input

Notes:
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        lindex = 0
        rindex = len(nums) - 1
        mindex = ((rindex - lindex) // 2) + lindex

        while lindex != rindex and rindex > lindex and lindex != mindex:
            if nums[mindex] == target:
                return mindex
            elif nums[mindex] > target:
                rindex = mindex
            elif nums[mindex] < target:
                lindex = mindex

            # find the middle, default to lower side when not whole
            mindex = ((rindex - lindex) // 2) + lindex

        if nums[lindex] == target:
            return lindex
        elif nums[rindex] == target:
            return rindex
        return -1
