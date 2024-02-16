import math


zone = int(input())
radius = int(input())
s1 = math.pi*zone**2
s2 = math.pi*radius**2
print(abs(s2-s1))