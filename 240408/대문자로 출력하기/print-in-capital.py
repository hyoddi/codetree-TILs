arr = input()
ans = ''

list(arr)
for i in arr:
    if i.isalpha() == True:
        ans += i.upper()

print(ans)