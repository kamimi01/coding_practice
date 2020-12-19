n, m = map(int, input().split())
hList = list(map(int, input().split()))

roadList = []
compareList = []

for i in range(m):
  a, b = map(int, input().split())
  roadList.append([a, b])
  compareList.append(max(a, b))

compareList = list(set(compareList))
print(compareList)

for j in range(m):
  for k in range(len(compareList)):
    targetMont = compareList[k]
    if roadList[j].count(targetMont) != 0:
      