x, n = map(int, input().split())
pList = list(map(int, input().split()))

if n == 0:
  print(x)
else:
  for i in range(0, 100):
    if x - i not in pList:
      print(x - i)
      break
    elif x + i not in pList:
      print(x + i)
      break

