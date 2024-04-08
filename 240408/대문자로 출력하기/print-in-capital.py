arr = input()
ans = ''

# print(ord('a') - ord('A')) = 32, 즉 소문자에 32를 빼면 대문자가 나온다.

for i in arr:
    if (i >= 'a' and i <= 'z') or (i >='A' and i<= 'Z'):
        ans+=i.upper()

print(ans)