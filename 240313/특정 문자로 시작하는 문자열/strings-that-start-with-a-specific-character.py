n = int(input())

arr=[]

for _ in range(n):
    tmp = input()
    arr.append(tmp)

val = input()

ans = [i for i in arr if i[0] == val]
ans2=0
for i in ans:
    ans2+=len(i)

print(f'{len(ans)} {ans2/len(ans):.2f}')