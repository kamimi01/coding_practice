import itertools
n = int(input())

dotList = []
for _ in range(n):
  x, y = map(int, input().split())
  dotList.append([x, y])

# print(dotList)


ans = 0

if n == 0:
  pass
else:
  for i in itertools.combinations(dotList, 2):
    katamukiList = list(i)
    # print(katamukiList)
    yKata = katamukiList[0][1] - katamukiList[1][1]
    xKata = katamukiList[0][0] - katamukiList[1][0]
    if -1 <= yKata / xKata <= 1:
      ans += 1

print(ans)
