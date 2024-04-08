A = input()
B = input()

a, b = '', ''

for i in A:
    if i.isalpha() == False:
        a += i

for j in B:
    if j.isalpha() == False:
        b += j

a = int(a)
b = int(b)

print(a + b)