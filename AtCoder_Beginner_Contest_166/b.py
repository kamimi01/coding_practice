n, k = map(int, input().split())

ans = 0
snackList = []

for i in range(k):
  d = int(input())
  # listを末尾に結合する（extend）
  snackList.extend(list(map(int, input().split())))

for j in range(n):
  number = j + 1
  if snackList.count(number) == 0:
    ans += 1

print(ans)
