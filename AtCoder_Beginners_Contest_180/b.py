import math

n = int(input())

x = list(map(int, input().split()))

manAns = 0

for i in range(len(x)):
  manAns += abs(x[i])
print(manAns)

yuAns = 0
tempYu = 0

for j in range(len(x)):
  tempYu += abs(x[j]) ** 2

print('{:.15f}'.format(math.sqrt(tempYu)))

absX = []
for k in range(len(x)):
  absX.append(abs(x[k]))

print(max(absX))
