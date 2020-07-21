import sys
N = int(sys.stdin.readline())
arr=[]
arr.append(0)
for i in range(N):
    arr.append(int(sys.stdin.readline()))
Dp=[0]

for i in range(1,3):
    if i == 1:
        Dp.append(arr[i])
        if N==1:
            break
        continue
    Dp.append(max(Dp[i-2]+arr[i],arr[i-1]+arr[i]))
for i in range(3,N+1):
    Dp.append(max(Dp[i-2]+arr[i],Dp[i-3]+arr[i-1]+arr[i]))
print(Dp[-1])
# print(Dp)