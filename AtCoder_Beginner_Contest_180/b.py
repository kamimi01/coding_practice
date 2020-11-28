import math

n = int(input())
x = list(map(int, input().split()))

manAns = 0
yuAns = 0
absX = []

for i in range(len(x)):
  # 絶対値を求める
  absXValue = abs(x[i])
  # マンハッタン距離
  manAns += absXValue
  # ユークリッド距離
  yuAns += absXValue ** 2
  # チェビシェフ距離
  absX.append(absXValue)

# マンハッタン距離
print(manAns)
# ユークリッド距離
print('{:.15f}'.format(math.sqrt(yuAns)))
# チェビシェフ距離
print(max(absX))
