N = int(input())

mulArr = []
for _ in range(N):
  arr = list(map(int, input().split(" ")))
  mulArr.append(arr)
# print(mulArr)

result = 0
for i in range(0, len(mulArr) - 2):
  # print(i)
  if mulArr[i][0] == mulArr[i][1] and mulArr[i + 1][0] == mulArr[i + 1][1] and mulArr[i + 2][0] == mulArr[i + 2][1]:
    result += 1

# print(result)
if result != 0:
  print("Yes")
else:
  print("No")
