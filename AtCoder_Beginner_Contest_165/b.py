import math
x = int(input())

targetMoney = x
currentMoney = 100
yearCounter = 0

while currentMoney < targetMoney:
  yearCounter += 1
  currentMoney += currentMoney // 100

print(yearCounter)
