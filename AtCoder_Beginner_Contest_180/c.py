n = int(input())


# 約数を求める関数
def make_divisors(n):
  lower_divisors, upper_divisors = [], []
  i = 1
  while i * i <= n:
    # 割り切れたら、lower_divisorのlistに格納する
    if n % i == 0:
        lower_divisors.append(i)
        if i != n // i:
            upper_divisors.append(n // i)
    i += 1
  return lower_divisors + upper_divisors[::-1]


ans = make_divisors(n)

for i in range(len(ans)):
  print(ans[i])
