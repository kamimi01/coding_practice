import numpy as np
h, w = map(int, input().split())

ans = 0
tenCount = 0
allArr = []

for i in range(h):
  wArr = list(input())
  allArr.append(wArr)
  # print(allArr)
  # 横の「.」の数を数える
  for j in range(w):
    if wArr[j] == ".":
      tenCount += 1
      if tenCount >= 2:
        ans += tenCount - 1
    else:
      tenCount = 0

arrNp = np.array(allArr)
# print(arrNp)

tateArr = []
tenCount2 = 0

for k in range(w):
  tateArr = []
  for l in range(h):
    tateArr.append(arrNp[l, k])
    # print(arrNp[l, k])
  # print(tateArr)

  # 横の「.」の数を数える
  for m in range(h):
    if tateArr[m] == ".":
      tenCount2 += 1
      if tenCount2 >= 2:
        ans += tenCount2 - 1
    else:
      tenCount2 = 0

print(ans)