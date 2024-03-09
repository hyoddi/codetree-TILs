N = int(input())

arr = list(map(int, input().split()))
answer=[]
max_num = 0

for idx, i in enumerate(arr):

    if i > max_num:
        
        answer.append(idx+1)
        max_num = i




for j in answer[::-1]:
    print(j, end= ' ')