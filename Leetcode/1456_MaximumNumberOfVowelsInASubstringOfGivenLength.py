"""
Problem Title: 1456. Maximum Number of Vowels in a Substring of Given Length
Platform: Leetcode
Problem URL:https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length?envType=study-plan-v2&envId=leetcode-75
Difficulty: Medium
Categories: String, Sliding Window, Weekly Contest 190
Author: Ryan Pelchat
Date Solved: 2025-08-28
Language: Python3

Problem Summary:
    Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

    Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.



    Example 1:

    Input: s = "abciiidef", k = 3
    Output: 3
    Explanation: The substring "iii" contains 3 vowel letters.

    Example 2:

    Input: s = "aeiou", k = 2
    Output: 2
    Explanation: Any substring of length 2 contains 2 vowels.

    Example 3:

    Input: s = "leetcode", k = 3
    Output: 2
    Explanation: "lee", "eet" and "ode" contain 2 vowels.



    Constraints:

        1 <= s.length <= 105
        s consists of lowercase English letters.
        1 <= k <= s.length



Approach:
    - strategy
        - sliding window
        - check vowel count in first substring
        - move window and subtract from vowel count if the char going
          out is a vowel and add to vowel count if the char coming in is
          a vowel
        - check vowel count in last substring
    - technique (two pointers, recursion, BFS, etc...)
        - sliding window
    - why did you choose it?
        - it is a linear streategy
    - edge cases considered?
        - the fist substring needs to be iterated through to start the
          count
        - the last substring needs to be iterated through to not cause
          the loop to go past the index

Time Complexity: 0(N)
Space Complexity: 0(1)

Notes:
"""

from typing import *


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        countMax = 0
        currentCount = 0

        for vowel in "aeiou":
            currentCount += s.count(vowel, 0, k)
        if currentCount > countMax:
            countMax = currentCount

        for i in range(len(s) - k):
            # print(f"Current: {s[i:i+k]}\tcc:{currentCount}\tincomming: {s[i+1:i+k+1]}")
            if s[i] in "aeiou":
                currentCount -= 1
                # print(f"sub1: {s[i]} in aeiou")
            if s[i + k] in "aeiou":
                currentCount += 1
                # print(f"add1: {s[i+k]} in aeiou")
            if currentCount > countMax:
                countMax = currentCount
            # print(f"Newcc: {currentCount}")

        currentCount = 0
        for vowel in "aeiou":
            currentCount += s.count(vowel, len(s) - k)

        if currentCount > countMax:
            countMax = currentCount

        return countMax
