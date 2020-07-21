N = int(input())
arr=[0]
ppp=[0]
for i in range(N):
    arr.append(int(input()))
for i in range(1,3):
    if i==1:
        ppp.append(arr[i])
        if N==1:
            break
        continue
    ppp.append(max(ppp[i-1],arr[i]+arr[i-1]))
for i in range(3,N+1):
    ppp.append(max(ppp[i-1],ppp[i-2]+arr[i],ppp[i-3]+arr[i-1]+arr[i]))
print(max(ppp))
# print(ppp)
