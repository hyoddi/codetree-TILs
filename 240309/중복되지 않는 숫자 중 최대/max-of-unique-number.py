N = int(input())

arr = list(map(int, input().split()))
ban = []
check = [-1]

for i in arr:

    if i in ban:
        check.remove(i)
        continue

    if i > check[-1]:
        check.append(i)

print(check[-1])