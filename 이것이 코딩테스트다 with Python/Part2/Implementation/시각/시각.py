n = int(input())
result = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if ('3' in str(i)) or ('3' in str(j)) or ('3' in str(k)):
                result += 1

print(result)

"""
참고) 7번 줄을 다음과 같이도 표현이 가능하다! 앞으로는 아래 표현을 사용하자.
if '3' in str(i) + str(j) + str(k):
"""
