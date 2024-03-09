N = int(input())

arr = list(map(int, input().split()))

check = [0 for _ in range(N)]
num = -1

for i in arr:

    check[i-1]+=1

for idx, j in enumerate(check):

    if j == 1 and idx + 1 > num:
        num = idx + 1

print(num)