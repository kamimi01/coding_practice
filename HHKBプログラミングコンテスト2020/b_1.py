h, w = map(int, input().split())

allArr = []
ans = 0

for i in range(h):
  wArr = list(map(str, input()))
  allArr.append(wArr)
print(allArr)

for j in range(h):
  for k in range(w):
    if k == w - 1:
      break
    if allArr[j][k] == "." and allArr[j][k + 1] == ".":
      ans += 1
    if j == h - 1:
      break
    if allArr[j][k] == "." and allArr[j + 1][k] == ".":
      ans += 1

print(ans)