import math
a, b, h, m = map(int, input().split())

hAngle = h * 30 + (m / 60) * 30
mAngle = m * 6

angle = abs(hAngle - mAngle)
if angle > 180:
  angle = 360 - angle

ans = math.sqrt(a ** 2 + b ** 2 - math.cos(math.radians(angle)) * 2 * a * b)

print(ans)
