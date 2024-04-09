n = int(input())
val = 0

for _ in range(n):
    tmp = int(input())
    val += tmp

val = str(val)

arr =[]

for i in val:
    arr.append(i)

tmp = arr.pop(0)

arr.append(tmp)

for i in arr:
    print(i,end = '')