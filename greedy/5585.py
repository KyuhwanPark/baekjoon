n = int(input())
coin = 1000-n
cnt = 0

while coin > 0:
    if coin >= 500:
        coin = coin - 500
        cnt += 1

    elif coin >= 100:
        coin = coin - 100
        cnt += 1

    elif coin >= 50:
        coin = coin - 50
        cnt += 1

    elif coin >= 10:
        coin = coin - 10
        cnt += 1

    elif coin >= 5:
        coin = coin - 5
        cnt += 1

    elif coin >= 1:
        coin = coin - 1
        cnt += 1

print(cnt)