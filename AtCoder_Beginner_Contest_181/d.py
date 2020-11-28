# わからん
from itertools import permutations

sList = list(map(str, input()))

ans = False

per = permutations(sList, 3)
for i in per:
  junList = list(i)
  strJunList = ''.join(junList)
  intJunList = int(strJunList)
  if intJunList % 8 == 0:
    ans = True
    break

if ans:
  print('Yes')
else:
  print('No')
