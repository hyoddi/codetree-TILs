A = input()

for i in A:
    if (i >= 'a' and i <= 'z'):
        print(i.upper(), end='')
    elif(i >= 'A' and i <= 'Z'):
        print(i.lower(), end='')