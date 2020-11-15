# 問題：https://qiita.com/gogotealove/items/11f9e83218926211083a
# みかん（100円）りんご（200円）ぶどう（300円）がそれぞれ1つずつ果物屋さんにありました。財布の中には300円ありますが、考え得るすべての買い物パターンを列挙しなさい。

money = 300
item = (("みかん", 100), ("りんご", 200), ("ぶどう", 300))
n = len(item)

# それぞれを買うか、買わないかなので2 ** 3 = 8通り
for i in range(2 ** n):
  # ここで必要なチェックを行う
  bag = []
  print("pattern {}:".format(i), end="")
  for j in range(n):
    if ((i >> j) & 1):
      bag.append(item[j][0])
  print(bag)
