a, b = map(int, input().split(" "))
seki = a * b

result = "Odd" if (seki % 2 != 0) else "Even"
print(result)
