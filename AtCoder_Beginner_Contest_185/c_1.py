l = int(input())

ans = 1

for i in range(11):
  ans *= (l - 1) - i
for j in range(1, 12):
  ans //= j

print(ans)
