n = int(input())
a_arr = list(map(int, input().split(" ")))

count = 0
flag = False

while True:
  for i in range(n):
    if a_arr[i] % 2 == 0:
      a_arr[i] //= 2
    else:
      print(count)
      flag = True
      break
  count += 1
  if flag:
    break
