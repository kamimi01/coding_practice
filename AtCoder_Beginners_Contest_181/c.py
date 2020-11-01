# これは間違いコード
n = int(input())

ansList = []

for i in range(n):
  x, y = map(int, input().split())
  ansList.append([x, y])

ansListX = []
ansListY = []
for j in range(n):
  ansListX.append(ansList[j][0])
  ansListY.append(ansList[j][1])

counter = 0
xJud = False
for k in range(n):
  counter = ansListX.count(k)
  if counter >= 3:
    xJud = True
    break

# print(xJud)

counterY = 0
yJud = False
for k in range(n):
  counterY = ansListY.count(k)
  if counterY >= 3:
    yJud = True
    break

# print(yJud)

if xJud == True or yJud == True:
  print('Yes')
else:
  print("No")
