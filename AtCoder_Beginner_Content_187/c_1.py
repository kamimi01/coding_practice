n = int(input())
s = set(input() for i in range(n))

for j in s:
  if "!" + j in s:
    print(j)
    exit()

print("satisfiable")