n = int(input())

arr = list(map(int, input().split()))
arr.reverse()

ans = ""
for i in range(n):
  if i == 0:
    ans += str(arr[i])
  else:
    ans += " " + str(arr[i])
print(ans)