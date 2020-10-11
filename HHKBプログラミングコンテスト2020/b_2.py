h, w = map(int, input().split())
s = [input() for _ in range(h)]

ans = 0

# 自分の右が"."であるかどうかを確認する
# なので、最後の１こは確認する必要がないのでw-1している
for i in range(h):
  for j in range(w - 1):
    if s[i][j] == "." and s[i][j + 1] == ".":
      ans += 1

# 自分の下が"."であるかどうかを確認する
# なので、最後の１こは確認する必要がないのでh-1している
for i in range(h - 1):
  for j in range(w):
    if s[i][j] == "." and s[i + 1][j] == ".":
      ans += 1

print(ans)
