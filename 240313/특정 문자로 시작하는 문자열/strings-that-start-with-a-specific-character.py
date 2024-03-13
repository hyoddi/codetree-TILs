n = int(input())

arr=[]
ans = 0

for _ in range(n):
    tmp = input()
    arr.append(tmp)

val = input()

for i in arr:
    print(i, arr)
    if i[0] == val:
        ans+=len(i)
    else:
        arr.remove(i)
    print(i, arr)

print(f'{len(arr)} {ans/len(arr):.2f}')