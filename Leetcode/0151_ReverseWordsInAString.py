"""
Problem Title: 151. Reverse Words in a String
Platform: Leetcode
Problem URL: https://leetcode.com/problems/reverse-words-in-a-string?envType=study-plan-v2&envId=leetcode-75
Difficulty: Medium
Categories: Two Pointers, String

Author: Ryan Pelchat
Date Solved: 2025-08-14
Language: Python3

Problem Summary:
    Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

Approach:
    - strategy
        - Very straitforward
        - Split string with " " delimeter
        - reverse list
        - join list with " " delimeter

Time Complexity: 0(N)
Space Complexity: 0(N)

Notes:
"""

from typing import *


class Solution:
    def reverseWords(self, s: str) -> str:
        reversed_string = reversed(s.split())
        return " ".join(reversed_string)
