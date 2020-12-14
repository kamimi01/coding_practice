import sys
n, m, t = map(int, input().split())

bat = n
time = 0

for _ in range(m):
  a, b = map(int, input().split())
  bat -= a - 