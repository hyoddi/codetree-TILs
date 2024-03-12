n = int(input())

arr=[]
val = 0

for _ in range(n):
    tmp = input()
    arr.append(tmp)

val = input()

for i in arr:
    if i[0] == val:
        print(len(i))
    else:
        arr.remove(i)
print(arr)
    


# print(f'{len(arr)} {val/len(arr):.2f}')