# 正解したけど、どれもTLEになってしまった
n, m, t = map(int, input().split())

ans = n
timeList = []

for j in range(m):
  x, y = map(int, input().split())
  timeList.append([x, y])

for i in range(m):
  a = timeList[i][0]
  b = timeList[i][1]
  # 出発から1回目のカフェまで
  if i == 0:
    timeCounter = 0
    counter = 0
    while timeCounter <= a:
      counter += 1
      if ans <= 0:
        break
      ans -= 1
      timeCounter = counter + 0.5

  # カフェにいる間
  timeCounter = 0
  counter = 0
  currentTime = a
  while currentTime + timeCounter <= b:
    counter += 1
    if ans <= 0:
        break
    if ans < n:
      ans += 1
    timeCounter = counter + 0.5
  
  # カフェ間の移動
  timeCounter = 0
  counter = 0
  currentTime = timeList[i][1]
  if i + 1 <= m - 1:
    while currentTime + timeCounter <= timeList[i + 1][0]:
      counter += 1
      if ans <= 0:
        break
      ans -= 1
      timeCounter = counter + 0.5

  # 最後のカフェから帰宅まで
  if i == m - 1:
    timeCounter = 0
    counter = 0
    currentTime = b
    while currentTime + timeCounter <= t:
      counter += 1
      if ans <= 0:
        break
      ans -= 1
      timeCounter = counter + 0.5

# 最後の判定
if ans > 0:
  print('Yes')
else:
  print('No')
