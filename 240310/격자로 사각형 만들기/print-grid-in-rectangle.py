n = int(input())

arr = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    arr[0][i] = 1
    arr[i][0] = 1


for i in range(1, n):
    for j in range(1, n):
        arr[j][i] = arr[j-1][i] + arr[j-1][i-1] + arr[j][i-1]




for i in arr:
    for j in i:
        print(j, end = ' ')
    print()