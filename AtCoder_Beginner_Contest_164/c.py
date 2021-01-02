n = int(input())
praiseList = []

for _ in range(n):
  s = input()
  praiseList.append(s)

praiseList = list(set(praiseList))

ans = len(praiseList)
print(ans)
