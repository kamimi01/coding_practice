a, b = map(str, input().split())

aAns = sum(list(map(int, list(a))))
bAns = sum(list(map(int, list(b))))

if aAns < bAns:
  print(bAns)
else:
  print(aAns)
