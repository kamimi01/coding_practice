sx, sy, gx, gy = map(int, input().split())

ans = (sy * gx + sx * gy) / (gy + sy)
print("{:.10f}".format(ans))
