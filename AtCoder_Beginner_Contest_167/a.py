s = input()
t = input()

sList = list(map(str, s))
tList = list(map(str, t))

ans = "Yes"

if len(sList) + 1 == len(tList):
  for i in range(len(sList)):
    if sList[i] != tList[i]:
      ans = "No"
      break
else:
  ans = "No"

print(ans)
