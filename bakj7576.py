import sys
from collections import deque
r = sys.stdin.readline
def bfs(M, N, arr):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    day = -1
    while queue:
        day+=1
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if (0<=nx<N) and (0<=ny<M) and (arr[nx][ny]==0):
                    arr[nx][ny] = arr[x][y] + 1
                    queue.append([nx,ny])
    for i in arr:
        if 0 in i:
            return -1

    return day

M, N = map(int, r().split())
arr = []
queue=deque()
for i in range(N):
    temp = list(map(int, r().split()))
    for j in range(M):
        if temp[j]==1:
            queue.append([i,j])
    arr.append(temp)



print(bfs(M,N,arr))
