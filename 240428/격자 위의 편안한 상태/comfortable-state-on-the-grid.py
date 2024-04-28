N, M = map(int, input().split())

arr = [[0 for _ in range(N)] for _ in range(N)]

# 동쪽부터 시계방향
dxs = [1, 0, -1, 0]
dys = [0, -1, 0, 1]

def in_range(tmpx, tmpy):
    return tmpx >= 0 and tmpx < N and tmpy >= 0 and tmpy < N

def check(nx, ny):
    cnt = 0
    for i in range(4):
        nx = nx + dxs[i]
        ny = ny + dys[i]
        
        # 범위 밖이라면 스킵
        if in_range(nx, ny) and arr[ny][nx] == 1:
            cnt+=1
    
    return cnt >= 3




for _ in range(M):
    r, c = map(int, input().split())
    y, x = r-1, c-1

    arr[y][x] = 1

    # 편안한 상태라면,
    if check(x, y): print(1)
    
    # 불편하다면
    else: print(0)


# for i in arr:
#     for j in i:
#         print(j, end = ' ')
#     print()