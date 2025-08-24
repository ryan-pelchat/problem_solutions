"""
Problem Title: 9. Palindrome Number
Platform: Leetcode
Problem URL: https://leetcode.com/problems/palindrome-number
Difficulty: Easy
Categories: Math

Author: Ryan Pelchat
Date Solved: 2025-08-23
Language: Python3

Problem Summary:
    Given an integer x, return true if x is a palindrome, and false otherwise.

    Example 1:

    Input: x = 121
    Output: true
    Explanation: 121 reads as 121 from left to right and from right to left.

    Example 2:

    Input: x = -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

    Example 3:

    Input: x = 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.



    Constraints:

        -231 <= x <= 231 - 1


    Follow up: Could you solve it without converting the integer to a string?

Approach:
    - strategy
        - convert integer into string
        - compare reversed string with non reversed string

Time Complexity: 0(N)
Space Complexity: 0(1)

Notes:
"""

from typing import *


class Solution:
    def isPalindrome(self, x: int) -> bool:
        number = str(x)
        return number == number[::-1]
        # if even length
        if len(number) % 2 == 0:
            # print(number[:len(number)//2+1] == number[len(number)//2:])
            # print(number[:len(number)//2])
            # print(number[-1:len(number)//2-1:-1])
            return number[: len(number) // 2] == number[-1 : len(number) // 2 - 1 : -1]
        else:
            # print(number[:len(number)//2])
            # print(number[-1:len(number)//2:-1])
            return number[: len(number) // 2] == number[-1 : len(number) // 2 : -1]
            # 1234321
