arr = list(input().split())

stack = []

for i in range(len(arr)):
  if arr[i] == "+":
    stack.append(stack.pop() + stack.pop())
  elif arr[i] == "-":
    stack.append(-(stack.pop() - stack.pop()))
  elif arr[i] == "*":
    stack.append(stack.pop() * stack.pop())
  else:
    stack.append(int(arr[i]))

print(stack[-1])
