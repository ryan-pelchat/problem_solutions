from typing import *

"""
Problem Title: Flood Fill
Platform: LeetCode
Problem URL: https://leetcode.com/problems/flood-fill/description/
Difficulty: Easy
Categories: Array, Depth-First Search, Breadth-First Search, Matrix

Author: Ryan Pelchat
Date Solved: 2025-06-13
Language: Python3

Problem Summary:
    You are given an image represented by an m x n grid of integers image,
    where image[i][j] represents the pixel value of the image. You are also
    given three integers sr, sc, and color. Your task is to perform a flood
    fill on the image starting from the pixel image[sr][sc].

To perform a flood fill:

    Begin with the starting pixel and change its color to color.
    Perform the same process for each pixel that is directly adjacent
    (pixels that share a side with the original pixel, either horizontally or
    vertically) and shares the same color as the starting pixel.
    Keep repeating this process by checking neighboring pixels of the updated
    pixels and modifying their color if it matches the original color of the
    starting pixel.
    The process stops when there are no more adjacent pixels of the original
    color to update.

Return the modified image after performing the flood fill.

Approach:
    - Depth-first search 
        - using a stack to keep track of nodes to visit
        - using a set to keep track of nodes visited and prevent looping

Time Complexity: 0(M * N)
    - where M and N are the sizes of sr and sc
Space Complexity: 0(M * N)
    - where M and N are the sizes of sr and sc

Notes:
"""


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:

        # Depth-first search

        coordsToChange = set()
        coordStack = [(sr, sc)]

        while len(coordStack) > 0:
            # take the top of stack
            # find all relevant adjacent squares that are not in coordsToChange
            # if no relevant squares then pop it
            # if relevant squares then push it onto stack
            relevantAdjacent = []
            top = coordStack[-1]
            # check center
            if (
                image[top[0]][top[1]] != color
                and (top[0], top[1]) not in coordsToChange
            ):
                coordsToChange.add((top[0], top[1]))
                relevantAdjacent.append((top[0], top[1]))

            # check above
            # shortcircuit if not possible, check if right number, check if already coloured, check if in our set
            if (
                top[0] > 0
                and len(image) > 1
                and image[top[0] - 1][top[1]] == image[top[0]][top[1]]
                and image[top[0] - 1][top[1]] != color
                and (top[0] - 1, top[1]) not in coordsToChange
            ):
                coordsToChange.add((top[0] - 1, top[1]))
                relevantAdjacent.append((top[0] - 1, top[1]))

            # check below
            elif (
                top[0] < (len(image) - 1)
                and image[top[0] + 1][top[1]] == image[top[0]][top[1]]
                and image[top[0] + 1][top[1]] != color
                and (top[0] + 1, top[1]) not in coordsToChange
            ):
                coordsToChange.add((top[0] + 1, top[1]))
                relevantAdjacent.append((top[0] + 1, top[1]))

            # check left
            elif (
                top[1] > 0
                and len(image[0]) > 1
                and image[top[0]][top[1] - 1] == image[top[0]][top[1]]
                and image[top[0]][top[1] - 1] != color
                and (top[0], top[1] - 1) not in coordsToChange
            ):
                coordsToChange.add((top[0], top[1] - 1))
                relevantAdjacent.append((top[0], top[1] - 1))

            # check right
            elif (
                top[1] < (len(image[0]) - 1)
                and image[top[0]][top[1] + 1] == image[top[0]][top[1]]
                and image[top[0]][top[1] + 1] != color
                and (top[0], top[1] + 1) not in coordsToChange
            ):
                coordsToChange.add((top[0], top[1] + 1))
                relevantAdjacent.append((top[0], top[1] + 1))

            if len(relevantAdjacent) == 0:
                coordStack.pop()
            else:
                coordStack.extend(relevantAdjacent[::])

        for coord in coordsToChange:
            image[coord[0]][coord[1]] = color
        return image
