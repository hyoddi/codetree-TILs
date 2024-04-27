N = int(input())

# 방향 딕셔너리
move_dir = {
    'E': 0,
    'S': 1,
    'W': 2,
    'N': 3
}

# 오른쪽부터 시계방향
dxs = [1, 0, -1, 0]
dys = [0, -1, 0, 1]

nowx, nowy = 0, 0

flag = 1
cnt = 0

for _ in range(N):
    
    tmp_dir, tmp_move = map(str, input().split())
    
    now_dir = move_dir[tmp_dir]
    now_move = int(tmp_move)

    for _ in range(now_move):
        nowx += dxs[now_dir]
        nowy += dys[now_dir]
        cnt+=1
        
        # print(f'({cnt}초 후: {nowx}, {nowy})')
        
        # 조건 만족 시 종료
        if nowx == 0 and nowy == 0:
            flag = -1
            break

    # 조건 만족 시 종료_이중 break
    if flag == -1:
        break

    

# 시작점 돌아왔다면
if flag == -1:
    print(cnt)

# 못 돌아왔다면
else:
    print(-1)