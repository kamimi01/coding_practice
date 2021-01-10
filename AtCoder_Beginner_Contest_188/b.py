n = int(input())
aList = list(map(int, input().split()))
bList = list(map(int, input().split()))

naiseki = 0
ans = "Yes"

for i in range(n):
  naiseki += aList[i] * bList[i]

if naiseki != 0:
  ans = "No"

print(ans)
