# これでも正解ではあったが、、実行時間に間に合わなかった....

n, q = list(map(int, input().split()))

mulArr = []
for _ in range(n):
  arr = list(input().split())
  mulArr.append(arr)

que = []       # 処理するキュー
done = []      # 処理が完了したもの
isDone = False  # 処理が完了したかどうか
time = 0       # 処理時間

for i in range(len(mulArr)):
  que.append(mulArr[i])

  leftProcess = int(mulArr[i][1]) - q

  if leftProcess > 0:
    que[-1][1] = str(leftProcess)
    time += q
  else:
    isDone = True
    time += int(mulArr[i][1])
    done.append(que[-1])
    que.pop()
    done[-1][1] = str(time)

print("1回目==========")

print("que1:{}".format(que))
print("done1:{}".format(done))

if len(que) != 0:
  while True:
    if len(que) == 0:
      break
    else:
      leftProcess = int(que[0][1]) - q
      print("leftProcess:{}".format(leftProcess))
      if leftProcess > 0:
        que[-1][1] = str(leftProcess)
        time += q
        print("que2:{}".format(que))
      else:
        isDone = True
        time += int(que[0][1])
        done.append(que[0])
        que.pop(0)
        done[-1][1] = str(time)
        print("que22:{}".format(que))
        print("done22:{}".format(done))
        


print("2回目==========")

print("que2:{}".format(que))
print("done2:{}".format(done))

# 出力
print("=====出力結果=======")
for k in range(len(done)):
  print("{} {}".format(done[k][0], done[k][1]))
