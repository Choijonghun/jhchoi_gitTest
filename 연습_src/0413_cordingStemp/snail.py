def snail():
  limit = int(input("열의 개수 입력 :"))
  tool = limit
  snail = [[0 for col in range(limit)] for row in range(limit)]
  x,y,direct ,num = 0,-1,1,1
  i = 0
  while True:
    for i in range(limit):
      y = y+direct
      snail[x][y] = num
      num = num + 1 
    limit = limit -1
    if limit<0: break
    for i in range(limit):
      x = x+ direct
      snail[x][y] = num
      num = num + 1 
    direct = -direct
  for i in range(tool):
    for j in range(tool):
      print(f"{snail[i][j]}\t",end='')
    print("\n")
