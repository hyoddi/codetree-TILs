n = input()
n = list(n)

for idx, i in enumerate(n):
    if i == 'e':
        n.pop(idx)
        break
    
ans = ''.join(n)

print(ans)