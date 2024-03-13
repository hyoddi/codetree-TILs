n = int(input())

arr = []

for _ in range(n):
    arr.append(input())

val = input()

new_arr = [i for i in arr if i[0] == val]
total_length = sum(len(s) for s in new_arr)
average_length = total_length / len(new_arr)

print(f'{len(new_arr)} {average_length:.2f}')