N = int(input())
A = list(map(int,input().split()))
M = int(input())
arr = list(map(int,input().split()))
A.sort()
for num in arr:
    l,r = 0,N-1
    isExist = False

    while l <= r:
        mid = (l+r)//2
        if num == A[mid]:
            isExist = True
            print(1)
            break
        elif num > A[mid]:
            l = mid+1  
        else:
            r = mid-1
    
    if not isExist:
        print(0)