n = int(input())
aList = list(map(int, input().split()))

# GCD度=kで割り切れた物の数
# その時のGCD度が最大になったkを出力する

counter = 0
ans = 0

for i in range(2, 1001):
  changeAList = list(map(lambda x: x % i, aList))
  zeroCounter = changeAList.count(0)
  if counter <= zeroCounter:
    counter = zeroCounter
    ans = i

print(ans)
