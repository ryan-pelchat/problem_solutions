"""
Problem Title: 392. Is Subsequence
Platform: Leetcode
Problem URL: https://leetcode.com/problems/is-subsequence?envType=study-plan-v2&envId=leetcode-75
Difficulty: Easy
Categories: Two Pointers, String, Dynamic Programming

Author: Ryan Pelchat
Date Solved: 2025-08-22
Language: Python3

Problem Summary:
    Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

    A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).



    Example 1:

    Input: s = "abc", t = "ahbgdc"
    Output: true

    Example 2:

    Input: s = "axc", t = "ahbgdc"
    Output: false



    Constraints:

        0 <= s.length <= 100
        0 <= t.length <= 104
        s and t consist only of lowercase English letters.


    Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?

    Approach:
        - strategy
            - pt1 that points to the first char in s that we seek
            - increment pt1 when we see it in t (as we loop through t)
            - if pt1 reaches end of s then return True, otherwise False
        - edge cases considered?
            - Empty string s needs to be considered,
                - return True, vaccuous truth

    Time Complexity: 0(N)
    Space Complexity: 0(1)

Notes:
    To answer the follow up question, I would start to compare future s
    to previous s instead of comparing every s to t. This is because s
    is usually smaller than t.
"""

from typing import *


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # pt1 is pointer pointing to the next char we are looking for in s
        # edge case: empty string
        if len(s) == 0:
            return True
        pt1 = 0
        for ch in t:

            if s[pt1] == ch:
                pt1 += 1

            if pt1 == len(s):
                return True

        return False
