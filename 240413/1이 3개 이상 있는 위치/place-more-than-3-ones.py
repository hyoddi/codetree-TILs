n = int(input())
arr=[]

dxs = [1, 0, -1 ,0]
dys = [0, -1, 0, 1]

ans = 0

def check_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n



for _ in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

for i in range(n):
    for j in range(n):
        
        cnt = 0

        for dx, dy in zip(dxs, dys):
            nx, ny = i + dx, j + dy
            if check_range(nx, ny) and arr[nx][ny] == 1:
                cnt+=1

        if cnt >= 3:
            ans+=1

print(ans)