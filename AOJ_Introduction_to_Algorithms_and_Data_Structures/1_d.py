n = int(input())

minv = 10 ** 18
maxv = -2000000000

for j in range(n):
  r = int(input())
  maxv = max(maxv, r - minv)
  minv = min(minv, r)

print(maxv)
