# 正解した!! 嬉しすぎる
from itertools import permutations

n = int(input())
ansList = []

for i in range(n):
  x, y = map(int, input().split())
  ansList.append([x, y])

ans = False

per = permutations(ansList, 3)
for i in per:
  junList = list(i)
  dx2 = junList[2][0] - junList[0][0]
  dy1 = junList[1][1] - junList[0][1]
  dx1 = junList[1][0] - junList[0][0]
  dy2 = junList[2][1] - junList[0][1]

  matsu = dx2 * dy1
  # print("matsu:", matsu)
  take = dx1 * dy2
  # print("take:", take)
  if matsu == take:
    ans = True
    break

if ans:
  print('Yes')
else:
  print('No')
