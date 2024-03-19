A = input()

ascii_num = ord(A)

if chr(ascii_num) == 'a':
    print('z')
else:
    print(chr(ascii_num - 1))