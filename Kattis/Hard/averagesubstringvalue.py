import bisect

string = input()

# below is assuming that there are at least 3 numbers

ls = [(int(string[i]), i) for i in range(len(string))]

ls.sort(key=lambda x: x[0])

totalNumberOfInputs = len(ls)

lsPoints = []  # will contain tuples where (i, il, ir)

lsSorted = []

while len(ls) > 0:
    index = bisect.bisect_left(lsSorted, ls[-1])
    # there are 3 possibilities, index is at start, middle, or end
    if index == len(lsSorted):  # then it is at the end
        # the right side is len(lsSorted)
        # find the left side
        right = totalNumberOfInputs - 1
        left = None
        if index != 0:
            left = lsSorted[index - 1]
