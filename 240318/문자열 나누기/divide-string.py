n = int(input())

arr=''

tmp = input().split()

for i in tmp:
    arr+=i


for idx in range(len(arr)):
    print(arr[idx], end='')
    if (idx+1) % 5 == 0:
        print()