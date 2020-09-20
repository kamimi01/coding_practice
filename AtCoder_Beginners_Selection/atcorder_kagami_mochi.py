N = int(input())
d_list = []

for i in range(N):
  d_list.append(int(input()))

last_d_list = list(set(d_list))

print(len(last_d_list))

# print(d_list)
