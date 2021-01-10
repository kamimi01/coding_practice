# 2問だけREになっちゃった
import copy
n = int(input())
aList = list(map(int, input().split()))
oriList = copy.copy(aList)

winList = []

while True:
  win = max(aList[0], aList[1])
  loser = min(aList[0], aList[1])
  # aListから2つの選手を除外する
  aList.remove(win)
  aList.remove(loser)
  # winListに勝った選手をいれる
  winList.append(win)
  # print(aList)
  # print(winList)
  if len(aList) <= 0:
    aList = winList
    if len(winList) == 2:
      lastWin = max(winList[0], winList[1])
      lastLoser = min(winList[0], winList[1])
      break
    else:
      winList = []

ans = oriList.index(lastLoser) + 1
print(ans)
