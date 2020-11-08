import math
from decimal import Decimal

a, b = map(Decimal, input().split())

ans = math.floor(a * b)
print(ans)
