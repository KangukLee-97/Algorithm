"""
6097: [기초-리스트] 설탕과자 뽑기
문제 Link: https://codeup.kr/problem.php?id=6097&rid=0

후기) 변수를 너무 많이 선언하고 사용했나..?
      굳이 튜플에 저장할 필요가 없었다고 생각한다.
      불필요한 선언은 없애자!
"""
h, w = map(int, input().split())  # 격자판의 세로와 가로
n = int(input())  # 놓을 수 있는 막대의 갯수
stick_arr = []
for _ in range(n):  # 각 막대의 길이, 방향, 좌표(x,y)
    stick_info = tuple(map(int, input().split()))
    stick_arr.append(stick_info)

# 격자판 초기화
matrix = [[0] * w for _ in range(h)]

# 각 막대 파악
for i in stick_arr:
    stick_x = i[2] - 1
    stick_y = i[3] - 1
    if i[1] == 0:  # 막대 방향이 가로
        for l in range(i[0]):
            matrix[stick_x][stick_y + l] = 1
    else:
        for l in range(i[0]):
            matrix[stick_x + l][stick_y] = 1

for i in range(h):
    for j in range(w):
        print(matrix[i][j], end=' ')
    print()
