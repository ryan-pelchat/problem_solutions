"""
Origin: https://www.eecs.yorku.ca/~jeff/courses/3101/
Problem in Dynamic Programming Slides

We want to print neatly a list of words.
The goal is to find the optimal arrangement of words. 
The optimal arrangement of words is found by providing a solution with the smallest cost.

Cost is the amount of space left on every line raised to the 3rd power add added together.
ex.
Be.sure.to. |   This has 1 space so cost is 1^3 = 1
be.honest.. |   This has 2 spaces so cost is 2^3 = 8
and.kind... |   This has 3 spaces so cost is 3^3 = 27
total cost = 1 + 8 + 27 = 36

input: list of words, maxLineLength
output: string with the optimal arrangement of words (where the newline symbols is used to separate lines)
"""

import math


def printNeatly(words: list[str], maxLineLength: int) -> str:
    pe = 3  # penalty exponent
    wordLengths = [len(word) for word in words]
    # The subInstance index is the subinstance
    # we do not store the optSolution because it takes too much space
    # we store just what we need to re-create optSolution
    subInstance = []  # birdAdvice and optimalCost

    # Base Case, printing 0 words
    subInstance.append(([], 0))

    # General Case, loop over subInstances
    for i in range(len(wordLengths)):
        # time to solve for this subinstance
        # try to fit everything on a newline, find how many words can we fit?
        K = 0
        for j in range(i, -1, -1):
            # slicing backwards, we are trying to fit words from j to i
            if (
                sum(wordLengths[j : i + 1]) + len(wordLengths[j : i + 1]) - 1
                > maxLineLength
            ):
                break
            else:
                K += 1
        # cycle through the bird answers (i.e. all possible words on this new line)
        # find optimal solution then save it to subInstance
        optimalSubinstace = ([], math.inf)
        for k in range(K):
            subInstanceIntermediate = (
                subInstance[i - k][0][::] + [k + 1],
                subInstance[i - k][1]
                + (
                    maxLineLength
                    - (
                        sum(wordLengths[i - k : i + 1])
                        + len(wordLengths[i - k : i + 1])
                        - 1
                    )
                )
                ** pe,
            )
            if subInstanceIntermediate[1] <= optimalSubinstace[1]:
                optimalSubinstace = subInstanceIntermediate
        subInstance.append(optimalSubinstace)

    # now we have the optimal solution
    # we reconstruct the solution
    print(subInstance)
    print(subInstance[-1])
    answer = ""
    currentWordIndex = 0
    for wordCountPerLine in subInstance[-1][0]:
        for i in range(wordCountPerLine):
            answer += words[currentWordIndex + i] + " "
        currentWordIndex += wordCountPerLine
        answer = answer[:-1] + "\n"
    return answer


if __name__ == "__main__":
    words = ["Love", "live", "man", "while", "there", "as", "we", "be"]
    M = 11
    print(printNeatly(words, M))


"""

def calc_words_size(wordSizes: list[int]) -> int:
    return sum(wordSizes) + len(wordSizes) - 1


def printNeatly(words: list[str], maxLineLength: int) -> str:
    pe = 3  # penalty exponent
    wordLengths = [len(word) for word in words]

    # subinstances are the words
    # for each subinstance, we need to remember the birdAnswers (edges) and the optimalCost for that subinstance
    subInstance = []

    # Base Case, there are 0 words to print
    subInstance.append(([], 0))

    # strategy:
    # pretend everything is added to a new line
    # if 0 then all words added to new line,
    # loop back to previous optimal answers incrementally to find current optimal answer
    # Now we loop over all subinstances, and for each, loop over each edge (birdAnswers)
    for i in range(len(wordLengths)):
        # solve for this instance
        # see how many words can fit on this new line
        K = 0
        for j in range(i, -1, -1):
            if calc_words_size(wordLengths[j : i + 1]) > maxLineLength:
                break
            else:
                K += 1
        # find optimal solution for this instance
        optimalSubinstance = ([], math.inf)
        for k in range(K):
            subInstanceIntermediate = (
                subInstance[i - k][0][::] + [k + 1],
                subInstance[i - k][1]
                + (maxLineLength - calc_words_size(wordLengths[i - k : i + 1])),
            )
            if subInstanceIntermediate[1] <= optimalSubinstance[1]:
                optimalSubinstance = subInstanceIntermediate
        subInstance.append(optimalSubinstance)
    return subInstance[-1]

"""
