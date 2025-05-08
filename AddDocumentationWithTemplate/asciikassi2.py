# https://open.kattis.com/problems/asciikassi2
"""
widths: 1, 3, 5
input: 0
 x pos 1 (2nd char)
x x width of 1
 x
input: 1
  x pos 2 (3rd char)
 / \
x   x width of 3
 \ /
  x
input: 2
   x pos 3 (4th char)
  / \
 /   \
x     x width of 5
 \   /
  \ /
   x

Strategy:
    - print top of diamond
    - print n sideLengths
    - print middle of diamond
    - print n sideLengths
    - print bottom of diamond
"""
sideLength = int(input())  # process input

# print top of diamond
print(" " * (sideLength + 1) + "x")

# print n sideLengths
for i in range(1, sideLength + 1):
    print(" " * (sideLength - i + 1) + "/" + " " * (2 * i - 1) + "\\")

# print middle of diamond
print("x" + " " * (2 * sideLength + 1) + "x")

# print n sideLengths
for i in range(sideLength, 0, -1):
    print(" " * (sideLength - i + 1) + "\\" + " " * (2 * i - 1) + "/")

# print bottom of diamond
print(" " * (sideLength + 1) + "x")
