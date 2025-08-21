"""
Problem Title: 443. String Compression
Platform: Leetcode
Problem URL: https://leetcode.com/problems/string-compression?envType=study-plan-v2&envId=leetcode-75
Difficulty: Medium
Categories: Two Pointers, String

Author: Ryan Pelchat
Date Solved: 2025-08-21
Language: Python3

Problem Summary:
    Given an array of characters chars, compress it using the following algorithm:

    Begin with an empty string s. For each group of consecutive repeating characters in chars:

        If the group's length is 1, append the character to s.
        Otherwise, append the character followed by the group's length.

    The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

    After you are done modifying the input array, return the new length of the array.

    You must write an algorithm that uses only constant extra space.



    Example 1:

    Input: chars = ["a","a","b","b","c","c","c"]
    Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
    Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

    Example 2:

    Input: chars = ["a"]
    Output: Return 1, and the first character of the input array should be: ["a"]
    Explanation: The only group is "a", which remains uncompressed since it's a single character.

    Example 3:

    Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
    Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".

    Constraints:

        1 <= chars.length <= 2000
        chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.

Approach:
    - strategy
        - 3 phases
            - phase 1 is counting the current char segment
            - phase 2 is creating the compressed char segment
            - phase 3 is ending compression when it reaches the end of chars
                - it also trims the end of the chars list to the appropriate size
        - pointer 1 keeps compressed writing location
        - pointer 2 is current point of reading uncompressed data
    - technique (two pointers, recursion, BFS, etc...)
        - 2 pointers
    - edge cases considered?
        - ending the compressed regions

Time Complexity: 0(N)
Space Complexity: 0(1)

Notes:
    - I decided to duplicate a little of my code in order to increase readability
    - phase 3 is similar to phase 1 but I decided to keep the separate so that it is easier to follow the logic
"""

from typing import *


class Solution:
    def compress(self, chars: List[str]) -> int:
        # 3 phases
        # phase 1 is counting segment of char
        # phase 2 is creating compressed record
        # phase 3 is ending compression when it reaches the end of chars
        # pointer 1 keeps compressed writing location
        # pointer 2 is current point of reading uncompressed data

        if len(chars) == 1:
            return 1

        pt1 = 0
        pt2 = 1
        currentCount = 1
        while pt1 < len(chars):
            # if the next segment is a new one
            if chars[pt1] != chars[pt2]:
                # store new values
                # increment pt1 to start writing char count
                # except if currentCount is 1
                if currentCount > 1:
                    pt1 += 1
                    for idx, count in enumerate(str(currentCount)):
                        chars[pt1 + idx] = count

                # move pt1 to new location to write
                pt1 += len(str(currentCount))

                # reset counter
                currentCount = 1

                # start new compressed segment
                chars[pt1] = chars[pt2]

                # increment pointer 2
                pt2 += 1
            else:  # still reading current segment
                # increment currentCount and pt2
                currentCount += 1
                pt2 += 1

            if pt2 >= len(chars):
                # store new values
                # increment pt1 to start writing char count
                # except if currentCount is 1
                if currentCount > 1:
                    pt1 += 1
                    for idx, count in enumerate(str(currentCount)):
                        chars[pt1 + idx] = count

                # move pt1 to new location to write
                pt1 += len(str(currentCount))

                # chop off uneeded uncompressed data
                chars = chars[:pt1]

        return pt1
