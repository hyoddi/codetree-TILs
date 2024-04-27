n , m = map(int, input().split()) # m이 x값, n이 y

arr = [[0 for _ in range(m)] for _ in range(n)]

# 오른쪽부터 시계방향 (행은 내려갈수록 커지는 걸 기억하자...)
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

# 처음 시작 위치 설정
x, y = 0, 0

# 현재 움직이는 방향 설정(오른쪽)
move_dir = 0

cnt = 1

def in_range(nc, nr):
    return nc >= 0 and nc < m and nr >= 0 and nr < n and arr[nr][nc] == 0

for _ in range(n*m):
    arr[y][x] = cnt

    tmpx = x + dxs[move_dir]
    tmpy = y + dys[move_dir]
    
    # 범위를 벗어나거나 숫자가 채워져있다면 방향 바꾸기
    if not in_range(tmpx, tmpy):
        move_dir = (move_dir + 1) % 4
        x += dxs[move_dir]
        y += dys[move_dir]
    
    # 범위 안이라면
    else:
        x, y = tmpx, tmpy
    
    cnt+=1
    
           



for i in arr:
    for j in i:
        print(j, end=' ')
    print()