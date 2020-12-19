n = input()

ans = []

for i in range(1, int(n) + 1):
  if '7' in str(i):
    ans.append(i)
  # 8進数に変換
  eightNum = format(i, 'o')
  # print(type(eightNum))
  if '7' in eightNum:
    # print(eightNum)
    ans.append(i)

ans = list(set(ans))
# print(ans)
print(int(n) - len(ans))
