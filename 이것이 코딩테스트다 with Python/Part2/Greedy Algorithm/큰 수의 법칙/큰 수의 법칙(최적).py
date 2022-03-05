# M의 크기가 100억 이상이면 다음 코드가 효율적이다!

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()   # 입력받은 수 정렬
first = data[n - 1]   # 가장 큰 수
second = data[n - 2]   # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
# k + 1은 가장 큰 수 k번과 두 번째로 큰 수 1번
# m을 k + 1로 나눈다는 것은 큰 수 k번과 두 번재로 큰 수 1번을 한 묶음으로 몇 번 계산이 가능한 것인지
count = int(m / (k + 1)) * k
count += m % (k + 1)   # m을 k+1로 나눴을 때 나누어 떨어지지 않았을 때는 큰 수만 남아있음

result = 0
result += (count * first)   # 가장 큰 수가 나온 횟수만큼 더하기
result += (m - count) * second   # 두 번째로 큰 수 더하기

print(result)