n = int(input())
intArr = list(map(int, input().split()))

# print(intArr)

ans = 0

for i in range(n + 1):
  makeArr = intArr[0:i]
  # if makeArr == []:
  #   break
  if makeArr.count(0) == 0:
    print(0)
  else:
    minNum = min(makeArr) + 1
    while True:
      if makeArr.count(minNum) == 0:
        print(minNum)
        break
      else:
        minNum += 1

