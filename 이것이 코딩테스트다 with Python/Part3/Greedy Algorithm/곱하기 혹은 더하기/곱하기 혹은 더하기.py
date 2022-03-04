num_list = input()
result = int(num_list[0])   # 첫 번째 문자를 숫자로 대입

for i in range(1, len(num_list)):
    if result < 2 or int(num_list[i]) < 2:   # 두 수 중에서 어떤 수라도 0또는 1인 경우에는 더하기가 효율적
        result += int(num_list[i])
    else:
        result *= int(num_list[i])

print(result)