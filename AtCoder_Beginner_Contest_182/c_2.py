# 正解のコード（解説通り）
import sys

n = input()
nList = list(map(int, n))

sum = sum(nList)
amari = sum % 3
amariList = list(map(lambda x: x % 3, nList))

if amari == 0:
  print(0)
elif amari == 1:
  # 余りが1の物を1つ消す
  if 1 in amariList:
    if len(nList) == 1:
      print(-1)
      sys.exit()
    print(1)
  # 余りが2の物を2つ消す（2が2つで、4になる。その余りが1）
  else:
    if len(nList) == 2:
      print(-1)
      sys.exit()
    print(2)
elif amari == 2:
  # 余りが2の物を1つ消す
  if 2 in amariList:
    if len(nList) == 1:
      print(-1)
      sys.exit()
    print(1)
  # 余りが1の物を2つ消す（1が2つで、2になる。その余りが2）
  else:
    if len(nList) == 2:
      print(-1)
      sys.exit()
    print(2)
