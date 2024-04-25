n, t = map(int, input().split())
r, c, d = map(str, input().split())
r ,c = int(r), int(c)

# 
dxs = [0, 1, -1, 0]
dys = [1, 0, 0, 1]


# 범위 안에 있으면 True, 없으면 False 반환
def check(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


# 딕셔너리 이용
mapper = {
    'R': 0,
    'D': 1,
    'U': 2,
    'L': 3
}

way = mapper[d]


arr = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(t):

    nx, ny = r + dxs[way], c + dys[way]
    if not check(nx, ny):
        way = 3 - way
        
    else:
        r, c = nx, ny 

print(r, c)