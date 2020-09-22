import math

r = float(input())

area = r ** 2 * math.pi
circle = r * 2 * math.pi

print("{:6f} {:6f}".format(area, circle))
