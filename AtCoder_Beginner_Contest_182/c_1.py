import sys

n = input()
nList = list(map(int, n))

sum = 0
amari = 0

for i in range(len(nList)):
  sum += nList[i]

if sum % 3 == 0:
  print(0)
  sys.exit()

for i in range(len(nList)):
  
