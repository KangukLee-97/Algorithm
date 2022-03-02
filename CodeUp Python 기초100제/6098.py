"""
6098: [기초-리스트] 성실한 개미
문제 Link: https://codeup.kr/problem.php?id=6098

개미는 오른쪽으로 움직이다가 벽을 만나면 아래쪽으로 움직인다.
(단, 가다가 오른쪽에도 길이 나타나면 다시 오른쪽으로 움직임)

상자 구조는 0(갈 수 있는 곳), 1(벽,장애물), 2(먹이 위치)

맨 아래의 가장 오른쪽에 도착한 경우, 더 이상 움직일 수 없는 경우, 먹이를 찾은 경우 => 그 곳에 머무름

출발지점: (2, 2)
"""
anthill = [[0] * 10 for _ in range(10)]
for i in range(10):
    anthill[i] = list(map(int, input().split()))

fin = 0
xpos, ypos = 1, 1

while fin == 0:
    if anthill[xpos][ypos] == 2:   # 지금 있는 자리가 먹이가 있는 자리라면
        anthill[xpos][ypos] = 9
        fin = 1
    else:   # 먹이가 있는 자리가 아니라면
        anthill[xpos][ypos] = 9   # 지금 있는 자리 방문처리
        if anthill[xpos][ypos+1] != 1:   # 오른쪽으로 갈 수 있다면
            ypos += 1
        else:   # 오른쪽으로 갈 수 없다면
            if anthill[xpos+1][ypos] != 1:   # 아래로 갈 수 있다면
                xpos += 1
            else:   # 아래로도 갈 수 없다면
                fin = 1


for i in range(10):
    for j in range(10):
        print(anthill[i][j], end=" ")
    print()