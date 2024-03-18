N = input()
arr = []

for idx in range(len(N)):
    if (idx+1) % 2 == 0:
        arr.append(N[idx])

for j in arr[::-1]:
    print(j,end= '')