A = input()

encoded = ''

l1  = A[0]
cnt = 1

for i in A[1:]:

    if i == l1:
        cnt+=1
    
    else:
        encoded += l1
        encoded += str(cnt)

        l1 = i
        cnt = 1

encoded += l1
encoded += str(cnt)

print(len(encoded))
print(encoded)