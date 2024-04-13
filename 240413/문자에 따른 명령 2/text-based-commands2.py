N = input()

x = 0
y = 0

# 동쪽부터 시계방향 (동남서북)
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# 북쪽을 바라보고 시작하기 때문
dir_num = 3

for i in N:
    if i == 'L':
        dir_num = (dir_num - 1 + 4) % 4  # dir_num이 0일 경우에 -1 % 4가 되는데, 언어에 따라 -1의 결과가 나올 수도 있어서.

    elif i == 'R':
        dir_num = (dir_num + 1) % 4
    
    elif i == 'F': 
        x += dx[dir_num]
        y += dy[dir_num]


print(x, y)