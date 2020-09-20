in_list = list(map(int, input().split(" ")))
N = in_list[0]
A = in_list[1]
B = in_list[2]

result = 0

for i in range(1, N + 1):
  i_arr = sum(list(map(int, list(str(i)))))
  # print(i_arr)
  if A <= i_arr <= B:
    result += i
  else:
    pass

print(result)
