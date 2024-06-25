from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int,input().split())

graph = [list(map(int,' '.join(input().split())))for _ in range(n)]
queue = deque([(0,0)])
dx = [-1,1,0,0]
dy = [0,0,-1,1]

while queue:
    x,y = queue.popleft() #큐 앞에서 노드 꺼냄
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1:
                queue.append((nx,ny)) # 큐의 뒤에 새로운 노드 추가
                graph[nx][ny] = graph[x][y]+1 # 거리 갱신
#결과 출력
print(graph[n-1][m-1])