n = int(input())

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
    ]

cnt = 1
u = 1

for i in range(n-1, -1, -1):

    if u == 1:
        for j in range(n-1, -1, -1):
            arr[j][i] = cnt
            cnt+=1
        u = -1
        
    
    elif u == -1:
        for j in range(n):
            arr[j][i] = cnt
            cnt+=1
        u = 1
        


for k in arr:
    for l in k:
        print(l, end = ' ')

    print()