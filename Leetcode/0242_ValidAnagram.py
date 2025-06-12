"""
Problem Title: Valid Anagram
Platform: Leetcode
Problem URL: https://leetcode.com/problems/valid-anagram/description/
Difficulty: Easy
Category: Hash Table, String, Sorting

Author: Ryan Pelchat
Date Solved: 2025-06-12
Language: Python3

Problem Summary:
    Given two strings s and t, return true if t is an
    of s, and false otherwise.

    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.

Approach:
    - 2 strings that are anagrams of each other have the exact same composition,
        i.e. same quantity and type of letters
    - change strings to a list, then sort them
        - if strings are equal then they also must be anagrams
        - if string are not equal then they are not anagrams

Time Complexity: 0(NlogN)
    - NlogN because that is the runtime of the sorting algorithm
Space Complexity: 0(N)
    - The strings are stored in memory and increases in a linear way
        according to the input

Notes:
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(list(s)) == sorted(list(t)):
            return True
        else:
            return False
