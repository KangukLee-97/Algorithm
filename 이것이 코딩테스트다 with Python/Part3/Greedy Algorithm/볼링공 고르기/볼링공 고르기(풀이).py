n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

# 각 무게에 해당하는 볼링공의 갯수 카운트
for i in data:
    array[i] += 1

result = 0

# 1부터 m까지의 각 무게에 대해서 처리
for i in range(1, m+1):
    n -= array[i]   # 무게가 i인 볼링공의 갯수(A가 선택할 수 있는 개수) 제외
    result += array[i] * n   # B가 선택하는 경우의 수와 곱하기

print(result)
