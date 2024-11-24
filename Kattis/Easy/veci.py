# Veci
"""
https://open.kattis.com/problems/veci?editresubmit=14988178
Your program will be given an integer X. Find the smallest number larger than X consisting of the same digits as X.
"""
from itertools import permutations

number = input()

# get all permutations of the number
perms = list(permutations(number))

# sort the permutations
permuations = []
for perm in perms:
    perm = int("".join(perm))
    if perm > int(number):  # no need for the ones larger than the number
        permuations.append(perm)

# sort the permutations
permuations.sort()

# check if there are no permuations larger than the numnber
if len(permuations) == 0:
    print(0)
    exit(0)
# print the smallest permutation larger than the number
print(permuations[0])
