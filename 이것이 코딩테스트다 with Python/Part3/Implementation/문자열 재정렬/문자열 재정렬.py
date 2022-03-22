data = input()
num_sum = 0

arr = []
for i in data:
    if ord(i) >= 65:   # 대문자 A 이상일 경우
        arr.append(i)
    else:
        num_sum += int(i)

arr.sort()   # 문자 오름차순 정렬
arr.append(str(num_sum))   # 끝에 숫자 더한거 붙임
print(''.join(arr))   # 리스트 출력
