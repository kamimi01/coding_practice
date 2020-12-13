# 正解したけど、全部TLEまたはMLEだった（MLEって初めて出た。メモリ制限に引っかかるレベルだったらしい）
import itertools

l = int(input())
splitPoint = l - 1

pList = list(itertools.combinations(range(splitPoint), 11))

print(len(pList))
