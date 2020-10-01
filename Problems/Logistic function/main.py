import math

x = int(input())

sigma = math.exp(x) / (math.exp(x) + 1)
result = round(sigma, 2)
print(result)