# 答えはあっているが、実行時間内に終わらない物がある
X, K, D = map(int, input().split())

for _ in range(K):
  if abs(X - D) < abs(X + D):
    X = X - D
  else:
    X = X + D

print(abs(X))