A = input()
op = input()


for i in range(len(op)):
    if op[i] == 'L':
        A = A[1:] + A[0]
    
    if op[i] == 'R':
        A = A[-1] + A[:-1]

print(A)