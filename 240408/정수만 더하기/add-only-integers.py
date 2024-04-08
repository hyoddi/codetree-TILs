A = input()
val=0
for i in A:
    if i.isalpha() == False:
        val += int(i)

print(val)