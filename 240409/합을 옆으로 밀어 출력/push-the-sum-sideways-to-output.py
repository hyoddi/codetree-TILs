n = int(input())
val = 0

for _ in range(n):
    tmp = int(input())
    val += tmp

val = str(val)

val = val[1:] + val[0]

print(val)