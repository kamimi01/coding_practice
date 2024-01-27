N, S = map(int, input().split())

result = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i * j <= S: result += 1

print(result)