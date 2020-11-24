n, m, x = map(int, input().split())

bookList = []
for _ in range(n):
  oneList = list(map(int, input().split()))
  bookList.append(oneList)

maxCost = 10 ** 3 * 12 + 1
minCost = maxCost

# bit全探索
for i in range(1, 2 ** n):
