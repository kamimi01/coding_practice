# 間違い!!（動画見ても、どこかの解説見ても理解できん）
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

ans = 0


def check(a, b, c, d):
  isOk = False
  if a + b == c + d or a - b == c - d or abs(a - c) + abs(b - d) <= 3:
    isOk = True
  return isOk


okResult = check(r1, c2, r2, c2)

# 少なくとも3手でどこでもいける
# パリティ（斜めに白と黒）の、白同志、黒同士であればどこでもいけるが
# 別の色に行くには必ず1手加ければいけないので、最大3手!!
if okResult:
  if r1 == r2 and c1 == c2:
    ans = 0
  else:
    ans = 1
# 2手でいけるのは、AB、AC、BC、CC
else:
  # AB（パリティが一緒）
  if abs(r1 + c1) == abs(r2 + c2) or abs(r1 - c1) == abs(r2 - c2):
    ans = 2
  # CC（マンハッタン距離が6以下）
  elif abs(r2 - r1) + abs(c2 - c1) <= 6:
    ans = 2
  # AC
  elif abs((r1 + c1) - (r2 + c2)) <= 3:
    ans = 2
  elif abs((r1 - c1) - (r2 - c2)) <= 3:
    ans = 2
  else:
    ans = 3

print(ans)
