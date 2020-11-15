import itertools

n, kyori = map(int, input().split())

tmpJunList = list(itertools.permutations(range(1, n + 1)))
junList = []

for j in range(len(tmpJunList)):
  if tmpJunList[j][0] == 1:
    listJunList = list(tmpJunList[j])
    junList.append(listJunList)

# print(junList)

timeList = []
for i in range(n):
  oneTimeList = list(map(int, input().split()))
  timeList.append(oneTimeList)

# print(timeList)

kotae = 0

for k in range(len(junList)):
  ans = 0
  for h in range(n - 1):
    i = junList[k][h]
    j = junList[k][h + 1]
    time = timeList[i - 1][j - 1]
    # print("時間は：", time)
    ans += time
    if h == n - 2:
      i = junList[k][n - 1] - 1
      time = timeList[i][0]
      # print("時間は：", time)
      ans += time
  # print(ans)
  if ans == kyori:
    kotae += 1
  # print("===")

# print("答え：", kotae)
print(kotae)

  