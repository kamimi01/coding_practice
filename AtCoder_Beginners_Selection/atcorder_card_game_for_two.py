N = int(input())
a_list = list(map(int, input().split(" ")))
a_list = sorted(a_list, reverse=True)

a_sum = 0
b_sum = 0

for i in range(N):
  if i == 0 or i % 2 == 0:
    a_sum += a_list[i]
  else:
    b_sum += a_list[i]

print(a_sum - b_sum)
