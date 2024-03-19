s = input()
new_s =''

first_char = s[1]

for i in range(0, len(s)):
    if s[i] == first_char:
        new_s+=s[0]
    else:
        new_s+=s[i]
    
print(new_s)