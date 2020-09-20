allS = int(input())

h = allS // 3600
m = allS % 3600 // 60
s = allS % 3600 % 60
print("{}:{}:{}".format(h, m, s))
