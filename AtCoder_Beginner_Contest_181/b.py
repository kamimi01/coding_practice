n = int(input())

ans = 0

# ガウスの足し算競争使った
for i in range(n):
  a, b = map(int, input().split())
  num = b - a + 1
  if num % 2 == 0:
    ans += (a + b) * (num // 2)
  else:
    ans += (a + b) * (num // 2) + ((a + b) // 2)
print(ans)
