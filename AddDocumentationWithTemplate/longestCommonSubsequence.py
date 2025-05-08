"""
Origin: https://www.eecs.yorku.ca/~jeff/courses/3101/
Problem in Dynamic Programming Slides

Given 2 strings without spaces, find the longest common subsequence between them.
"""

# def printSub(instance):
#     for i in instance:
#         print(i)


def longestCommonSubsequence(word1: str, word2: str) -> str:
    # create the data matrix
    subInstances = [[0 for __ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]

    # loop over subInstances
    for i in range(1, len(subInstances)):
        for j in range(1, len(subInstances[0])):
            # check for the 3 cases, reject left, reject right, or accept current
            if word1[i - 1] == word2[j - 1]:
                subInstances[i][j] = subInstances[i - 1][j - 1] + 1
            subInstances[i][j] = max(
                [subInstances[i - 1][j], subInstances[i][j - 1], subInstances[i][j]]
            )

    # now reconstruct optimal solution, walking backwards
    i, j = len(subInstances) - 1, len(subInstances[0]) - 1
    str = ""
    while i > 0 and j > 0:
        if word1[i - 1] == word2[j - 1]:
            str += word1[i - 1]
            i -= 1
            j -= 1
        elif subInstances[i - 1][j] > subInstances[i][j - 1]:
            i -= 1
        else:
            j -= 1
    # printSub(subInstances)
    return str[::-1]


if __name__ == "__main__":
    word1 = "asbetchda"
    word2 = "rtwabjcktfd"
    print(longestCommonSubsequence(word1, word2))
