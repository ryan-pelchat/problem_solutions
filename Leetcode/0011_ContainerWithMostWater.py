"""
Problem Title: 11. Container With Most Water
Platform: Leetcode
Problem URL: https://leetcode.com/problems/container-with-most-water?envType=study-plan-v2&envId=leetcode-75
Difficulty: Medium
Categories: Array, Two Pointers, Greedy

Author: Ryan Pelchat
Date Solved: 2025-08-23
Language: Python3

Problem Summary:
    You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

    Find two lines that together with the x-axis form a container, such that the container contains the most water.

    Return the maximum amount of water a container can store.

    Notice that you may not slant the container.

    **picture here**

    Example 1:

    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

    Example 2:

    Input: height = [1,1]
    Output: 1



    Constraints:

        n == height.length
        2 <= n <= 105
        0 <= height[i] <= 104



Approach:
    - strategy
        - Used 2 pointers, pt1 at start and pt2 at end
        - Shorter side is the limiting factor, so move it until it isn't
        - Throughout keep track of max area value
    - technique (two pointers, recursion, BFS, etc...)
        - 2 pointers
    - why did you choose it?
    - edge cases considered?

Time Complexity: 0(N)
Space Complexity: 0(1)

Notes:
"""

from typing import *


class Solution:
    def maxArea(self, height: List[int]) -> int:
        currentMax = 0
        pt1 = 0
        pt2 = len(height) - 1

        while pt1 < pt2:
            tempArea = self.calcArea(pt1, pt2, height)
            if tempArea > currentMax:
                currentMax = tempArea
            if height[pt1] < height[pt2]:
                pt1 += 1
            else:
                pt2 -= 1
        return currentMax

    def calcArea(self, pt1: int, pt2: int, heights: List[int]) -> int:
        """Returns area of rectangle drawn by the values at pt1 and pt2 in heights

        Parameters:
        pt1: int
            First index that corresponds to a value in heights
        pt2: int
            Second ndex that corresponds to a value in heights

        Invariant:
            pt1 < pt2

        Returns
        int
            Total area drawn between the 2 values at pt1 and pt2 locations in heights
            One side length is the min of the 2 values and the other is the difference in indexes
        """
        return min(heights[pt1], heights[pt2]) * (pt2 - pt1)
