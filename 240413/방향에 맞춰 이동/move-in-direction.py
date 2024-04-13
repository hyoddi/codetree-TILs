N = int(input())

nx = 0
ny = 0

def op(w, n):
    global dx, dy, nx, ny
    if w == 'E':
        nx += n

    elif w == 'S':
        ny -= n

    elif w == 'W':
        nx -= n

    elif w == 'N':
        ny += n


for _ in range(N):
    way, num = map(str, input().split())
    num = int(num)
    op(way, num)

print(nx, ny)