#a의 최솟값과 b의 최댓값 곱하기.
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort()
sum = 0
for i in range(n):
    max_b = max(b)
    sum += a[i] * max_b
    b.remove(max_b)

print(sum)