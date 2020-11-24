r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

ans = 0


def check(a, b, c, d):
  isOk = False
  if a + b == c + d or a - b == c - d or abs(a - c) + abs(b - d) <= 3:
    isOk = True
  return isOk


okResult = check(r1, c2, r2, c2)

if okResult:
  if r1 == r2 and c1 == c2:
    ans = 0
  else:
    ans = 1
else:
  