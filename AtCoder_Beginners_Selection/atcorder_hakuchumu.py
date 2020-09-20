s = input()
erase_dream_arr = ["eraser", "erase", "dreamer", "dream"]

for value in erase_dream_arr:
  s = s.replace(value, "")

if s:
  print("NO")
else:
  print("YES")