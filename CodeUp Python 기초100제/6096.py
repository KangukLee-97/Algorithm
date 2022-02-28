"""
6097: [기초-리스트] 바둑알 십자 뒤집기
문제 Link: https://codeup.kr/problem.php?id=6096
"""
# 바둑판 초기화
baduk = [[0] * 19 for _ in range(19)]
for i in range(19):
    baduk[i] = list(map(int, input().split()))

n = int(input())   # 십자 뒤집기 횟수

for i in range(n):
    x, y = map(int, input().split())

    for j in range(19):
        if baduk[x-1][j] == 0:
            baduk[x-1][j] = 1
        else:
            baduk[x - 1][j] = 0

        if baduk[j][y-1] == 0:
            baduk[j][y-1] = 1
        else:
            baduk[j][y-1] = 0

for i in range(19):
    for j in range(19):
        print(baduk[i][j], end=" ")
    print()
