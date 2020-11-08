x, y = map(int, input().split())

ans = "No"

for i in range(x + 1):
  j = x - i
  if 2 * i + 4 * j == y:
    ans = "Yes"

print(ans)
