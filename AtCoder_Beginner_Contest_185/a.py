a1, a2, a3, a4 = map(int, input().split())

ans = 0

if a1 == 0 or a2 == 0 or a3 == 0 or a4 == 0:
  pass
else:
  ans = min([a1, a2, a3, a4])

print(ans)
