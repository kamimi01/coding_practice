# 自分のコードでも正解したが、こちらの方がスマート
import itertools

n, k = map(int, input().split())

time = []
for i in range(n):
  tmpTime = list(map(int, input().split()))
  time.append(tmpTime)

nums = list(range(1, n))
perm = itertools.permutations(nums)
ans = 0

for index in perm:
  index = [0] + list(index)
  ti = 0
  # print(index)
  for i in range(n):
    # i + 1がnになった場合（つまり3 + 1 = 4）の場合、n=4で割れば、余りが0になるので、[0]が抽出できる
    ti += time[index[i]][index[(i + 1) % n]]
  if ti == k:
    ans += 1

print(ans)
