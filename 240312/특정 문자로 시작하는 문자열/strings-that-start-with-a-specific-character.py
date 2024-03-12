n = int(input())

arr=[]
ans = 0

for _ in range(n):
    tmp = input()
    arr.append(tmp)

val = input()

for i in arr:
    if i[0] == val:
        ans+=len(val)
    else:
        arr.remove(i)

print(f'{len(arr)} {ans/len(arr):.2f}')