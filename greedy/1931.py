#1개의 회의실 -> 가장 빨리 끝나는 거 먼저
import sys
N = int(input())
arr = []
for i in range(N):
    start,end = map(int,sys.stdin.readline().split())
    arr.append((start,end))
arr.sort(key = lambda x : (x[1],x[0]))

ans = [arr[0]]

i = 0
for j in range(1,len(arr)):
    if arr[j][0] >= arr[i][1]:
        ans.append(arr[j])
        i = j
print(len(ans))