N = int(input())
list = list(map(int, input().split()))

sum = 0
for i in list:
    sum += i

print(sum % 100)