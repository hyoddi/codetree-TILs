N = int(input())
arr = list(map(int, input().split()))

max_num = -1

for i in arr:
    if i > max_num:
        cnt = 0

        for j in arr:
            if j == i:
                cnt+=1
        
        if cnt == 1:
            max_num = i
print(max_num)