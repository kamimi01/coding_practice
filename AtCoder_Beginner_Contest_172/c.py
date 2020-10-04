# 実行時エラーやWrong Answerが
from collections import deque

n, m, k = map(int, input().split())
aDeq = deque(list(map(int, input().split())))
bDeq = deque(list(map(int, input().split())))
# print(aDeq, bDeq)

count = 0
sumMin = 0
while sumMin <= k:
  if len(aDeq) == 0 and len(bDeq) == 0:
    break
  elif len(aDeq) == 0 or aDeq[0] > bDeq[0]:
    count += 1
    sumMin += bDeq[0]
    bDeq.popleft()
  elif len(bDeq) == 0 or aDeq[0] < bDeq[0]:
    count += 1
    sumMin += aDeq[0]
    aDeq.popleft()
  if sumMin > k:
    count -= 1

print(count)
