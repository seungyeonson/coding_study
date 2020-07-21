def bfs(start, visited, cnt):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    queue=[]
    queue.append(start)
    while queue:
        x,y = queue.pop(0)
        visited[x][y] = cnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx <N and 0<=ny<N and visited[nx][ny]==0 and arr[nx][ny]==arr[x][y]:
                queue.append([nx,ny])
                visited[nx][ny]=cnt


N = int(input())
arr = []
for _ in range(N):
    arr.append(list(input()))
visited_1 = [[0]*N for _ in range(N)]
visited_2 = [[0]*N for _ in range(N)]
answer_1=0
answer_2=0
for i in range(N):
    for j in range(N):
        if visited_1[i][j]==0:
            # print(answer_1)
            answer_1+=1
            bfs([i,j],visited_1,answer_1)

for i in range(N):
    for j in range(N):
        if arr[i][j]=='G':
            arr[i][j]='R'
for i in range(N):
    for j in range(N):
        if visited_2[i][j]==0:
            answer_2 += 1
            bfs([i, j], visited_2, answer_2)
print(answer_1,answer_2)