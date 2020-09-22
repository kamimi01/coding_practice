from queue import Queue

# 1行目の標準入力
n, q = map(int, input().split())
# Queueオブジェクトの作成
que = Queue()

# 2行目以降の標準入力
for i in range(n):
  name, time = input().split()
  # Queueオブジェクトへの格納
  que.put((name, int(time)))

total = 0
# Queueに要素が存在する限り繰り返す
while que.qsize() > 0:
  name, time = que.get()
  # クオンタムと処理時間のうち、値の小さい方を合計処理時間に追加する
  total += min(q, time)

  if q < time:
    # 処理時間がクオンタムよりも大きい場合は、処理時間からクオンタムを引いてQueueに再格納する
    que.put((name, time - q))
  else:
    # 処理時間がクオンタム以内になる場合は、処理が終了しているので、出力を行う
    print(name, total)
