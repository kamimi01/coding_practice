n, m, t = map(int, input().split())

ans = n
timeList = []

for j in range(m):
  x, y = map(int, input().split())
  timeList.append([x, y])

now = 0
leftBattery = n
