A = input()

ascii_num = ord(A)

if char(ascii_num) == 'a':
    print('z')
else:
    print(char(ascii_num - 1))