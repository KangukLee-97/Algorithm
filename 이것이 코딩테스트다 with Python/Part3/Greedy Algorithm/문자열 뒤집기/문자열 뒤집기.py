num_str = input()
first = num_str[0]   # 맨 첫번째 문자
count0 = 0   # 모두 0으로 바꾸는 경우
count1 = 0   # 모두 1로 바꾸는 경우

if first == '1': count0 += 1
else: count1 += 1

# 두 번째 원수부터 모든 원소 확인
for i in range(len(num_str)-1):
    if num_str[i] != num_str[i+1]:
        # 다음 수에서 1로 바뀌는 경우
        if num_str[i+1] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))