# 残り13分までがんばってみたけど、できなかった。。やっぱDはむずいな
# とりあえず最初のサンプルだけは通ったぞ
n = int(input())
aList = list(map(int, input().split()))

sumAList = sum(aList)
hikuBun = 0
ans = 0
heruNum = 1

for i in range(n):
  if i == n - 1:
    break
  hikuBun += aList[i]
  tmpAns = abs(aList[i] * (n - heruNum) - (sumAList - hikuBun))
  ans += tmpAns
  heruNum += 1

print(ans)
