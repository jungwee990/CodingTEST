from collections import deque

n,m = map(int, input().split())

# 2차원리스트 생성
graph = []
for i in range(n):
  graph.append(list(map(int,input())))

# 상하좌우 방향
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
  queue = deque()
  queue.append((x,y))

  # q가 빌때까지
  while queue:
    (x,y) = queue.popleft() #
    

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      # 생성된 맵의 바깥으로 나가는 경우 무시
      if nx >=n or nx < 0 or ny >= m or ny <0: 
        continue  
      # 이동하려는 노드가 벽인경우 무시
      if graph[nx][ny] == 0:
        continue
      
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y]+1
        queue.append((nx,ny))

  return graph[n-1][m-1]
      
print(bfs(0,0))