n = int(input())

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
    ]

cnt = 1

for i in range(n-1, -1, -1):

    if i % 2 == 1:
        for j in range(n-1, -1, -1):
            arr[i][j] = cnt
            cnt+=1
    
    if i % 2 == 0:
        for j in range(n):
            arr[i][j] = cnt
            cnt+=1
    
    

for i in arr:
    for j in i:
        print(j, end = ' ')
    
    print()