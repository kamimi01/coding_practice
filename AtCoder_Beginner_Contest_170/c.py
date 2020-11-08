import sys

x, n = map(int, input().split())
pList = list(map(int, input().split()))

if n == 0:
  print(x)
  sys.exit()

ansPlu = x
ansMin = x

while(True):
  ansPlu += 1
  if ansPlu not in pList:
    break

while(True):
  ansMin -= 1
  if ansMin not in pList:
    break

# print(ansPlu, ansMin)
# print(min(ansPlu, ansMin))

saPlu = abs(x - ansPlu)
saMin = abs(x - ansMin)

if saPlu == saMin:
  print(min(ansPlu, ansMin))
elif saPlu < saMin:
  print(ansPlu)
elif saPlu > saMin:
  print(ansMin)
