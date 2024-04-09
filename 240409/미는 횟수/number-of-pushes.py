A = input()
B = input()
flag = -1
cnt = 0

for _ in range(len(A)):
    if A == B:
        flag = 1
    else:
        A = A[1:] + A[0]
        cnt+=1

if flag == -1:
    print(flag)
else:
    print(cnt)