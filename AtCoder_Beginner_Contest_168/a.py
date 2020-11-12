n = input()
nList = list(map(int, n))

last = nList[-1]
ans = ""

if last == 2 or last == 4 or last == 5 or last == 7 or last == 9:
  ans = "hon"
elif last == 0 or last == 1 or last == 6 or last == 8:
  ans = "pon"
else:
  ans = "bon"

print(ans)
