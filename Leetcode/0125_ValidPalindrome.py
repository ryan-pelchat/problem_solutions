"""
Problem Title: Valid Palindrome
Platform: Leetcode
Problem URL: https://leetcode.com/problems/valid-palindrome/description/
Difficulty: Easy
Category: Two Pointers, String

Author: Ryan Pelchat
Date Solved: 2025-06-06
Language: Python3

Problem Summary:
    A phrase is a palindrome if, after converting all uppercase letters into lowercase
    letters and removing all non-alphanumeric characters, it reads the same forward and
    backward. Alphanumeric characters include letters and numbers.

    Given a string s, return true if it is a palindrome, or false otherwise.

Approach:
    - 2 pointers one at start and one at end
    - each pointer moves towards the center checking that it is a palindrome
    - if the pointers cross each other without differences then return true, otherwise false
    - when moving the pointer, the pointers need to skip over the non-alphanumeric characters

    - I choose this approach because it is of linear runtime and constant memory
    - This approach does not modify the original string

Time Complexity: 0(N)
    - The 2 pointers only move towards each other until they reach each other
Space Complexity: 0(1)
    - At most I create an additional 2 ints for the pointers
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1 = 0  # pointer 1
        p2 = len(s) - 1  # pointer 2

        # advance p1 to first alphanumeric character
        while p1 < len(s) and not s[p1].isalnum():
            p1 += 1

        # advance p2 to first alphanumeric character
        while p2 > 0 and not s[p2].isalnum():
            p2 -= 1

        while p1 != p2 and p2 > p1:
            if s[p1].upper() != s[p2].upper():
                return False
            p1 += 1
            p2 -= 1
            # advance p1 to first alphanumeric character
            while p1 < len(s) and not s[p1].isalnum():
                p1 += 1

            # advance p2 to first alphanumeric character
            while p2 > 0 and not s[p2].isalnum():
                p2 -= 1

        return True
