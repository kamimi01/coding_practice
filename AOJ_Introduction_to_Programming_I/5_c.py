while True:
  H, W = map(int, input().split())
  if H == 0 and W == 0:
    break
  for i in range(H):
    if i % 2 == 0:
      result = ""
      for j in range(W):
        if j % 2 == 0:
          result += "#"
        else:
          result += "."
      print(result)
    else:
      resultOther = ""
      for k in range(W):
        if k % 2 == 0:
          resultOther += "."
        else:
          resultOther += "#"
      print(resultOther)
    if i == H - 1:
      print()
