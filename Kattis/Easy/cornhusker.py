# https://open.kattis.com/problems/cornhusker?editresubmit=14991591

"""
Wordy but once you figure out what they want, it is not too bad.
The way it is worded is confusing, but the problem is simple.
"""


cornVals = list(map(int, input().split()))
rows, kwf = map(int, input().split())
totAvg = 0
for x in range(0, len(cornVals), 2):
    totAvg += cornVals[x] * cornVals[x + 1]

totAvg = totAvg // 5

print(rows * totAvg // kwf)
