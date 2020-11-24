n, x = map(int, input().split())
sList = list(map(str, input()))

ans = x

for i in range(n):
  if sList[i] == "o":
    ans += 1
  else:
    ans -= 1
  if ans <= 0:
    ans = 0

print(ans)
