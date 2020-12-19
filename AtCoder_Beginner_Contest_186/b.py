h, w = map(int, input().split())

blockList = []
for _ in range(h):
  yokoList = list(map(int, input().split()))
  blockList = blockList + yokoList

minBlockNum = min(blockList)

ans = 0
for i in range(h * w):
  hikuBlock = blockList[i] - minBlockNum
  ans += hikuBlock

print(ans)
