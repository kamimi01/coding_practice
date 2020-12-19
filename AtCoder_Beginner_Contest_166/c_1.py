n, m = map(int, input().split())
hList = list(map(int, input().split()))

roadList = []
for j in range(n):
  roadList.append(set())
# print(roadList)

for i in range(m):
  a, b = map(int, input().split())
  roadList[a - 1].add(b - 1)
  roadList[b - 1].add(a - 1)

ans = 0

for k in range(n):
  res = True
  for x in roadList[k]:
    # 比較して低い山であれば、良い山にはならないのでFalse
    if hList[k] <= hList[x]:
      res = False
      break
  if res:
    ans += 1

print(ans)
