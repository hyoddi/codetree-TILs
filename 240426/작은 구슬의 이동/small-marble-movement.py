n, t = map(int, input().split())
r, c, d = map(str, input().split())
r ,c = int(r), int(c)

# 3 - 현재 방향을 빼면 뒤집힐 수 있도록 설정

dys = [1, 0, 0, -1] # 행, x값
dxs = [0, 1, -1, 0] # 열, y값


# 범위 안에 있으면 True, 없으면 False 반환
def check(x, y):
    return x > 0 and x <= n  and y > 0 and y <= n


# 딕셔너리 이용
mapper = {
    'R': 0,
    'U': 1,
    'D': 2,
    'L': 3
}

# 방향 초기값 설정 
way = mapper[d]

for _ in range(t):

    ny = r + dxs[way] # 행
    nx = c + dys[way] # 열


    if not check(nx, ny):
        way = 3 - way
    
    else:
        r, c = ny, nx
    
    

print(r, c)