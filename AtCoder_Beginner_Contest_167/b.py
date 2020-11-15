a, b, c, k = map(int, input().split())

ans = 0

if a >= k:
  ans += 1 * k
else:
  ans += 1 * a
  k = k - a
  if b >= k:
    ans += 0 * k
  else:
    ans += 0 * b
    k = k - b
    if c >= k:
      ans += -1 * k
    else:
      ans += -1 * c

print(ans)
