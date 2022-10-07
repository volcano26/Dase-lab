import math
import random
c = float(2)
h = 0.00001
i = random.uniform(0,2)
while pow(i,2) > c or pow((i+1),2) < c:
    i = random.uniform(0,2)
while c - pow(i,2) > 0.0001:
    i += h
print(i)

min = 0
max = c
j = random.uniform(0,2)
while abs(pow(j,2) - c) > 0.0001:
    if pow(j,2) > c:
        max = j
    else:
        min = j
    j = (max + min) / 2
print(j)

t = c / 2
while abs(pow(t,2) - c) > 0.0001:
    t = (t + (c / t) ) / 2
print(t)