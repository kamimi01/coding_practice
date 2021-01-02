n = int(input())
sList = []

ans = "satisfiable"

for _ in range(n):
  s = input()
  sList.append(s)
# print(sList)

for i in range(n):
  target = sList[i]
  if target.startswith("!"):
    target = target.lstrip("!")
  else:
    target = "!" + target
  # print(target)
  if target in sList:
    ans = sList[i]
    if ans.startswith("!"):
      ans = ans.lstrip("!")
    break

print(ans)
