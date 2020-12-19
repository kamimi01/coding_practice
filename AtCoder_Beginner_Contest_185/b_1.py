import sys
n, m, t = map(int, input().split())

bat = n
time = 0

for _ in range(m):
  a, b = map(int, input().split())
  bat -= a - time
  # 0以下になったらNoになる
  if bat <= 0:
    print('No')
    sys.exit(0)
  # 0以下にならなければ、減らしたバッテリ量にカフェにいる間の充電分を足す。
  # ただしもし元のバッテリー量を超えたらそれ以上は増えないので、nになる
  bat = min(n, bat + (b - a))
  # 前いったカフェを出た時間をtimeに格納する
  time = b

# 最後に残ったバッテリ量が、bat - (t - time)である
# それが0以下になった場合はNoになる
if bat - (t - time) <= 0:
  print('No')
# 0以下にならなければYesになる
else:
  print('Yes')
