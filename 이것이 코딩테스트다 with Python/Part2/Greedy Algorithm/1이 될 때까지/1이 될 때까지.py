N, K = map(int, input().split())  # N과 K 입력받기
count = 0

while N >= K:
    if N % K != 0:  # 나누어 떨어지지 않는다면
        while N % K != 0:   # 나누어 떨어질 때까지
            N -= 1   # N을 1씩 빼준다
            count += 1
    N //= K   # K로 나누기
    count += 1

while N != 1:   # 남은 부분에서 N이 1이 될 때까지 빼준다
    N -= 1
    count += 1

print(count)