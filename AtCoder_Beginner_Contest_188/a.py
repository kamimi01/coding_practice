x, y = map(int, input().split())

add = min(x, y)
ans = "Yes"

if add == x:
  if x + 3 > y:
    pass
  else:
    ans = "No"
else:
  if y + 3 > x:
    pass
  else:
    ans = "No"

print(ans)
