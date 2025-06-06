from typing import *

"""
Problem Title: Invert Binary Tree
Platform: LeetCode
Problem URL: https://leetcode.com/problems/invert-binary-tree/description/
Difficulty: Easy
Category: Tree, Depth-First Search, Breadth-First Search, Binary Tree

Author: Ryan Pelchat
Date Solved:
Language: Python3

Problem Summary:
    Given the root of a binary tree, invert the tree, and return its root.

Approach:
    - Create a recursive algorithm that travels through the tree and swaps children
    - Careful that the base case covers if the root is None, or if it has no children
    - Careful that the base case only return root iff both children are None
        - because then you can recurse down one of the children

Time Complexity: 0(N)
    - The algorithm needs to switch every children in the whole tree
Space Complexity: 0(N)
    - The algorithm recurses as many times as the depth of the tree
"""


# Definition for a binary tree node.
# the class TreeNode is provided from LeetCode
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # base case
        if root is None or (root.left is None and root.right is None):
            return root

        # recursive case
        else:
            root.left, root.right = root.right, root.left
            if root.left is not None:
                self.invertTree(root.left)
            if root.right is not None:
                self.invertTree(root.right)
        return root
