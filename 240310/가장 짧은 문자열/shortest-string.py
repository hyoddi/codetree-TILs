check = []
for _ in range(3):
    tmp = str(input())
    check.append(len(tmp))

print(max(check) - min(check))