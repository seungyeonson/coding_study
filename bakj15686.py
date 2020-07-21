from itertools import combinations
def bfs(arr,ms):
    visit=[[2*N]*N for _ in range(N)]
    queue=ms
    while queue:
        temp = queue.pop(0)
        x = temp[0]
        y = temp[1]
        for i in range(N):
            for j in range(N):
                if arr[i][j]==0:
                    visit[i][j]=0
                elif arr[i][j]==2:
                    visit[i][j]=0
                elif arr[i][j]==1:
                    new = abs(x-i)+abs(y-j)
                    if visit[i][j]>new:
                        visit[i][j] = new
    return sum_arr(visit)

def sum_arr(array):
    number=0
    for i in range(len(array)):
        number+=sum(array[i])
    # print(array)
    # print(number)
    return number

def dist(arr,ms,M):
    if len(ms)==M:
        print(bfs(arr,ms))
    elif len(ms)>M:
        combi = list(combinations(ms,M))

        print(combi)
        number=10000000
        for i in range(len(combi)):
            # print("ee",list(list(combi[i])))
            temp = bfs(arr,list(combi[i]))
            if temp<number:
                number= temp
        print(number)




N, M = map(int, input().split())
arr=[]
ms=[]

for _ in range(N):
    arr.append(list(map(int, input().split())))
for i in range(N):
    for j in range(N):
        if arr[i][j]==2:
            ms.append([i,j])
dist(arr,ms,M)
