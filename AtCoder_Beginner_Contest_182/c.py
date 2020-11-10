import sys

n = input()
nList = list(map(int, n))

sum = 0
amari = 0

for i in range(len(nList)):
  sum += nList[i]

amari = sum % 3
if amari == 0:
  print(0)
  # print("tomaruyo")
  sys.exit()

ans = 0

if nList.count(amari) >= 1:
  print(1)
  # print("1だよ")
else:
  for i in range(len(nList)):
    # print("elseだよ")
    if ans >= 1:
      break
    hiku = nList[i] - amari
    if hiku >= 0:
      if (nList[i] - amari) % 3 == 0:
        ans += 1
    else:
      if len(nList) == 2:
        ans = -1
        break
      ans = 2
  print(-1 if ans == 0 else ans)
