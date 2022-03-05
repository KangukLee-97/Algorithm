n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort(reverse=True)   # 내림차순으로 정렬
result = 0

first = data[0]   # 가장 큰 수
second = data[1]   # 두 번째로 큰 수

# 총 m번 더해야 한다. 하지만 가장 큰 수를 k번 초과해서 더하면 안된다.
while True:
    for i in range(k):   # k번 동안 first를 더함
        if m == 0:
            break
        result += first
        m -= 1   # 수행 횟수 1씩 제거
    if m == 0:
        break
    result += second   # second를 한번 더해줌
    m -= 1

print(result)