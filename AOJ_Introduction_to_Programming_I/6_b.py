n = int(input())

sArr = []
hArr = []
cArr = []
dArr = []

for i in range(n):
  pair = list(input().split())
  # print(pair)
  sArr.append(pair)
  tmpSArr = [s for s in sArr if "S" in s]

print(tmpSArr)

for j in range(1, 14):
  print("出す")
  if str(j) in tmpSArr:
    
    print(j)

# スペードの1~13が存在するか調べる。なければprintする
# for j in range(1, 14):
#   for k in range(len(tmpSArr)):
#     if str(j) not in tmpSArr[k]:
#       print("S {}".format(str(j)))

# print(arr)


    


# spade:1~13
# heart:1~13
# club:1~13
# dia:1~13