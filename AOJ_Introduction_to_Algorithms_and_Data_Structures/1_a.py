n = int(input())
originList = list(map(int, input().split()))

print(originList)

for i in range(1, n):
  # 要素iの中身
  v = originList[i]
  # iから1引いたインデックス
  j = i - 1
  # jが0以上かつ、最初の配列の[j]が[i]より大きい限りは、
  while (j >= 0 and originList[j] > v):
    # iとjを入れ替える
    originList[j + 1] = originList[j]
    j -= 1
    originList[j + 1] = v
  print(originList)