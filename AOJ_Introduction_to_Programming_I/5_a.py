while True:
  H, W = map(int, input().split())
  if H == 0 and W == 0:
    break
  for _ in range(H):
    regtangle = ""
    for _ in range(W):
      regtangle += "#"
    print(regtangle)
  print()
