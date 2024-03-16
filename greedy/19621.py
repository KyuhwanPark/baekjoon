import sys
N = int(input())
arr = []
for i in range(N):
    start,end,person = map(int,sys.stdin.readline().split())
    arr.append((start,end,person))
    arr.sort(key=lambda x:(x[1],x[2]))

dp = [0]*N  #최대 인원
dp[0] = arr[0][2]
for i in range(1,N):
    dp[i] = max(dp[i-1],dp[i-2]+arr[i][2])

print(dp[N-1])