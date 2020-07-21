# Botom-up
T = int(input())

for case in range(T):
    arr = [1, 2, 4]

    N = int(input())
    for i in range(3, N):
        arr.append(sum(arr[i - 3:i]))
        # print(i,arr[i])
    print('answer', arr[N - 1])