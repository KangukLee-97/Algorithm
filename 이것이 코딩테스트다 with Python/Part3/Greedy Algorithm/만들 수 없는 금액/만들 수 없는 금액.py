n = int(input())   # 동전의 개수
coin = list(map(int, input().split()))   # 화폐 단위
coin.sort()

result = 1

for i in coin:
    if result < i:   # 만들 수 없는 금액을 찾았을 때
        break
    result += i

print(result)
