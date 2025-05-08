# https://open.kattis.com/problems/rectanglearea
"""
Given diagonal corners of a rectangle with sides parallel to the 
 and 
 axes, compute the area of the rectangle.
"""
coords = list(map(float, input().split()))  # process input

# compute area of rectangle
area = abs(coords[0] - coords[2]) * abs(coords[1] - coords[3])
print(area)  # output result
