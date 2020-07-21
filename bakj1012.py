import sys
r = sys.stdin.readline
def bfs(array, queue, visit, answer):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while queue:
        i,j = queue.pop(0)
        if array[i][j]>0 and visit[i][j]==0:
            array[i][j] = answer
            visit[i][j] = 1
            for n in range(4):
                x = i+dx[n]
                y = j+dy[n]
                if (0<=x< N) and (0<=y<M) and array[x][y]==1:
                    queue.append([x,y])

    return


T = int(input())



for case in range(T):
    M, N, K = map(int, r().split())
    arr = [[0 for j in range(M) ] for i in range(N)]
    visit = [[0 for j in range(M) ] for i in range(N)]
    for _ in range(K):
        j,i = map(int,r().split())
        arr[i][j]=1
    # print(arr)
    queue=[]
    answer=0
    for i in range(N):
        for j in range(M):
            if visit[i][j]==0 and arr[i][j]>0:
                queue.append([i,j])
                answer+=1
                bfs(arr,queue,visit,answer)
    print(answer)