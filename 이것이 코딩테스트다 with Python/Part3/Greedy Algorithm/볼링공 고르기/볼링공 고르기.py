n, m = map(int, input().split())   # 볼링공의 갯수, 공의 최대 무게
k = list(map(int, input().split()))   # 각 볼링공의 무게
count = 0

for i in range(n):
    for j in range(i+1, n):
        if k[i] != k[j]:
            count += 1

print(count)
