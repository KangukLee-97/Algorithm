n, m = map(int, input().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

min_list = []   # 각 행에서의 최솟값들을 저장할 리스트
for i in range(n):
    min_list.append(min(matrix[i]))

print(max(min_list))