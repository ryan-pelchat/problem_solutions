"""
Problem Title: Longest Substring Without Repeating Characters
Platform: Leetcode
Problem URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
Difficulty: Medium
Category: Hash Table, String, Sliding Window

Author: Ryan Pelchat
Date Solved: May 8th 2025
Language: Python3

Problem Summary:
    Given a string s, find the length of the longest without duplicate characters.

Approach:
    - Use a sliding window to find the longest subsequence
    - Use 2 indexes that point to start and end of window
    - Loop through string, if next char in str is in window (defined by start and end indexes)
        - yes: then shorted left side of window until duplicate is removed
        - no: then exted right side of window to encompass new char
    - Keep the maximum running total that was ever reached
    - When the str has been looped through, then return the maximum running total

Time Complexity: 0(...)
    O(N^2), this is because in the worst case, s[lid:rid] takes O(N) and it is loop for N char in str
Space Complexity: 0(...)
    O(N), This is because all variables are constant size and slicing can only be as big as the str

Notes:
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        lid = 0
        rid = 0
        lmax = 0
        for c in s:
            if c in s[lid:rid]:
                lid = lid + s[lid:rid].find(c) + 1
            rid += 1
            if (rid - lid) > lmax:
                lmax = rid - lid
        return lmax
