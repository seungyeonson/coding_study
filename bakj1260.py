#BFS
#BFS는 같은거리에 있는 노드를 우선으로 방문하는 것이다.
#DFS
#DFS는 깊잉우선하여 탐색하는 방법이다.
N, M, V = map(int, input().split())
arr = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    link = list(map(int, input().split()))
    arr[link[0]][link[1]] = 1
    arr[link[1]][link[0]] = 1

def dfs(current_node, arr, visit):
    visit += [current_node]
    for search_node in range(len(arr[current_node])):
        if arr[current_node][search_node] and search_node not in visit:
            # visit += [search_node]
            visit = dfs(search_node, arr, visit)
    return visit


def bfs(start):
    queue = [start]
    visit = [start]
    while queue:
        node = queue.pop(0)
        for search_node in range(len(arr[node])):
            if arr[node][search_node] and search_node not in visit:
                visit += [search_node]
                queue += [search_node]
    return visit


print(*dfs(V, arr, []))
print(*bfs(V))

