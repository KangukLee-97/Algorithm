n, k = map(int, input().split())
result = 0

while True:
    # (N == K로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k   # ex) 17 4일 경우 4의 배수중에서 17에 가장 가까운 수를 찾는 코드
    result += (n - target)   # N이 k로 나누어 떨어질 수 있게까지 빼는 횟수 더함
    n = target
    # N이 K보다 작을 때(더이상 나눌수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대해서 1씩 빼기
result += (n - 1)
print(result)