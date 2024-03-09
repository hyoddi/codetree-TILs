N = int(input())

arr = list(map(int, input().split()))
arr.append(-1)
ban = []

while(True):

    tmp = max(arr)

    if arr.count(tmp) > 1 or tmp in ban:
        arr.remove(tmp)
        ban.append(tmp)
        continue
    
    break

        
print(max(arr))