def bfs(arr, start, end):
    while queue:
        current_node = queue.pop(0)

        if current_node == K:
            return arr[K]

        for j in [current_node + 1, current_node - 1, current_node * 2]:
            if 0 <= j <= Max and arr[j] == 0:
                arr[j] = arr[current_node] + 1
                queue.append(j)

    return arr[K]


N, K = map(int, input().split())
Max = 100000
arr = [0] * (Max + 1)
queue = [N]
print(bfs(arr, N, K))
