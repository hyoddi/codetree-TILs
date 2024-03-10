# 주어진 두 줄의 문자열 입력 받기
line1 = input()
line2 = input()

# 두 줄의 문자열을 하나의 문자열로 합치기
combined_string = line1 + " " + line2

# 합쳐진 문자열에서 공백 제거하기
result = combined_string.replace(" ", "")

# 결과 출력
print(result)