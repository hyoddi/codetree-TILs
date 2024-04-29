N, B = map(str, input().split())
B = int(B)
ans = 0

for i in range(len(N)):
    x = N[i]
    if ord(x) >= ord('0') and ord(x) <= ord('9'):
        tmp = int(x)
    else:
        tmp = ord(x) - 55
    
    print(B**(len(N) - i - 1))
    ans += (B**(len(N) - i - 1)) * tmp

print(ans)