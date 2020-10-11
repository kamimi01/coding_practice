n = int(input())
p = list(map(int, input().split()))

result = []
t = 0
# 重複は無視して、一意な値のみ保存される（生成時の順序は保証されない）
s = set()

for i in p:
  s.add(i)
  # tがsetオブジェクとに存在する限り繰り返す
  while t in s:
    t += 1
  result.append(t)

for j in result:
  print(j)
