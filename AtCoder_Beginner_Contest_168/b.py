k = int(input())
s = input()

kList = list(map(str, s))

ans = s

if len(kList) <= k:
  pass
else:
  first = kList[0:k]
  ans = "".join(first) + "..."

print(ans)
