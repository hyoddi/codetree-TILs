n = input()
new_n = ''
flag = -1

for i in range(len(n)):
    if n[i] == 'e' and flag == -1:
        flag = 1
        continue
    new_n+=n[i]

print(new_n)