import sys

N, K = map(int, sys.stdin.readline().split())

coins = []
cnt = 0

for i in range(N):
    coins.append(int(input()))
    coins.sort(reverse=True)

for coin in coins:
    if K // coin > 0:
        cnt += K // coin
        K = K % coin


print(cnt)