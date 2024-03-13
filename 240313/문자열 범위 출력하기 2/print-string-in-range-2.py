l = input()
reverse_l = l[::-1]
n = int(input())

if n > len(reverse_l):
    print(reverse_l)
else:
    for i in range(n):
        print(reverse_l[i], end= '')