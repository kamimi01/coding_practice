N = int(input())

result = 0

# c = 1
# b = 1

for c in range(1, N):
  print("c:" + str(c))
  for b in range(1, N - c + 1):
    print("b:" + str(b))
    if (N - c) % b != 0:
      break
    result += 1
    
    # if (N - c) % b != 0:
    #   break
    # a = (N - c) / b
    # if a * b + c != N:
    #   break
    # result += 1

print(result)

# while True:
#   if (N - c) % b != 0:
#     break
#   a = (N - c) / b
#   if (N - c) / b == a:
#     result += 1
#     print(a, b, c)
#     c += 1
#     # b += 1
#   else:
#     break

# print(result)