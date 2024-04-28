op = input()

# 북쪽부터 시계방향
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

x ,y = 0 ,0

# 북쪽을 바라바고 시작
move_dir = 0

flag = -1

direction = {
    'L': -1,
    'R': 1
}

cnt = 1


for i in op:

    if i == 'F':
        x += dxs[move_dir]
        y += dys[move_dir]

    else:
        move_dir = (direction[i] + move_dir) % 4    

    # 0,0 으로 돌아오면 종료
    if x == 0 and y == 0:
        flag = 1
        break
    cnt += 1


if flag == 1:
    print(cnt)
else:
    print(flag)