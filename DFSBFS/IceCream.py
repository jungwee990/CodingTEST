n,m = map(int, input().split())

# 2차원리스트의 맵정보 입력받기
graph = []
for i in range(n):
  graph.append(list(map(int, input())))

def dfs(x,y):
  if x<=-1 or x>=n or y <= -1 or y>=m:
    return False
  # 특정노드에 방문후 상하좌우 방문
  if graph[x][y] == 0:
    graph[x][y] = 1

    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    return True

  return False

# 생성한 얼음수 카운트
count = 0
for i in range(n):
  for j in range(m):
    if dfs(i,j) == True:
      count += 1
      
print(count)

  