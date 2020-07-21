def bfs(arr, start):
    queue=[]
    queue.append(start)
    while queue:
        i = queue.pop(0)
        
    return

N, M = map(int,input().split())
arr = dict()
visited = []
for i in range(1,N+1):
    arr[i] = [i]
for i in range(M):
    l,r = map(int, input().split())
    if l not in visit or r not in visit:
        arr[l].append(r)
        arr[r].append(l)
    elif l  in visit and r in visit:
        pass
for i in range(1,N+1):
    print(arr[i])

