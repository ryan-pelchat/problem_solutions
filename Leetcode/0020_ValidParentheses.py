"""
Problem Title: Valid Paraentheses
Platform: Leetcode
Problem URL: https://leetcode.com/problems/valid-parentheses/description/
Difficulty: Easy
Category: ---

Author: Ryan Pelchat
Date Solved: May 8th 2025
Language: Python3

Problem Summary:
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
        Every close bracket has a corresponding open bracket of the same type.


Approach:
    - Use a stack, push and pop to match brackets
    - Be careful of edge cases where:
        - empty str
        - more close brackets than open brackets
        - len(str) is 1


Time Complexity: 0(...)
    O(N)
Space Complexity: 0(...)
    O(N)

Notes:
    The timestamps are the amount of time I took to come up with that solution
"""


class Solution:
    # 7:40
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return False
        pairings = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for c in s:
            if c in "({[":
                stack.append(c)
            elif c in ")}]":
                if len(stack) == 0 or pairings[stack.pop()] != c:
                    return False
        if len(stack) > 0:
            return False
        return True
