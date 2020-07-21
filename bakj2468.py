vx = [0, 0, -1, 1]
vy = [1, -1, 0, 0]
def bfs(arr, queue, visit, number, count):
    while queue:
        i, j = queue.pop(0)
        if arr[i][j]>number and visit[i][j]==0:
            visit[i][j]=count

            for n in range(4):
                x = i + vx[n]
                y = j + vy[n]
                if (0<=x< N) and (0<=y<N) and arr[x][y]>number:
                        queue.append([x,y])

N = int(input())
maps = []
queue=[]
sets=set()
answer = 0



for i in range(N):
    temp = list(map(int, input().split()))
    maps.append(temp)
    for j in range(len(temp)):
        sets.add(temp[j])
sets = list(sets)
sets.append(0)
for n in range(len(sets)):
    number = sets[n]
    visit = [[0 for j in range(N) ] for i in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if visit[i][j]==0 and maps[i][j]>number:
                queue.append([i,j])
                count+=1
                bfs(maps, queue, visit, number,count)
    if answer < count:
        answer = count
print(answer)