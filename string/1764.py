n, m = map(int, input().split())
name_set = set()
ans_set = set()

for _ in range(n):
    name = input()
    name_set.add(name)

for _ in range(m):
    name = input()
    if name in name_set:
        ans_set.add(name)

ans_list = sorted(list(ans_set))
print(len(ans_list))
for name in ans_list:
    print(name)