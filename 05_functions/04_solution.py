import math

def circle_stats(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

# print(circle_stats(5))

a, c = circle_stats(5)
print("Area: ", round(a, 2), "Circumference: ", round(c, 2))
