def bfs(start, end):
    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [2, 1, -1, -2, -2, -1, 1, 2]
    queue = []
    queue.append(start)
    visited[start[0]][start[1]] = 1
    while queue:

        x, y = queue.pop(0)
        if x == end[0] and y == end[1]:
            return visited[x][y] - 1

        for i in range(8):
            ax = x + dx[i]
            ay = y + dy[i]
            if 0 <= ax < I and 0 <= ay < I and visited[ax][ay] == 0:
                queue.append([ax, ay])
                visited[ax][ay] = visited[x][y] + 1


T = int(input())

for case in range(T):
    I = int(input())
    visited = [[0] * I for _ in range(I)]
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    print(bfs(start, end))