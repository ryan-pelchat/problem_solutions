"""
Problem Title: 345. Reverse Vowels of a String

Platform: Leetcode
Problem URL: https://leetcode.com/problems/reverse-vowels-of-a-string?envType=study-plan-v2&envId=leetcode-75
Difficulty: Easy
Categories: Two Pointers, String

Author: Ryan Pelchat
Date Solved:
Language: Python3

Problem Summary:
    Given a string s, reverse only all the vowels in the string and return it.

    The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Approach:
    - strategy
        - Go through list record vowels and respective indices
        - reverse vowels list
        - replace with new vowels at respective indices

Time Complexity: 0(N)
Space Complexity: 0(N)

Notes:
    - Could have used 2 pointers scanning from both ends and swapping chars along the way
    - This would have saved some space and time, but it would still be O(N) for both
"""

from typing import *


class Solution:
    def reverseVowels(self, s: str) -> str:
        indexes = []
        vowels = []
        strIn = [x for x in s]
        for idx, ch in enumerate(s):
            if ch in "aeiouAEIOU":
                indexes.append(idx)
                vowels.append(ch)
        vowels.reverse()
        for i in range(len(vowels)):
            strIn[indexes[i]] = vowels[i]
        return "".join(strIn)
