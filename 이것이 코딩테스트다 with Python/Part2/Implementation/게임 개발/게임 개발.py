n, m = map(int, input().split())   # 맵의 세로와 가로크기
x, y, d = map(int, input().split())   # 캐릭터 좌표, 방향

matrix = []   # 맵 정보
visited = [[0] * m for _ in range(n)]   # 방문 표

for i in range(n):   # 맵 정보 입력
    matrix.append(list(map(int, input().split())))

# 북쪽, 동쪽, 남쪽, 서쪽
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 1   # 방문한 칸의 수
turn_count = 0   # 캐릭터가 이동이 가능한지 확인하는 변수

# 처음 있는 곳 방문 처리
visited[x][y] = 1


# 왼쪽으로 도는 함수
def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3


while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]

    # 방문하지 않은 곳이고 육지라면
    if visited[nx][ny] == 0 and matrix[nx][ny] == 0:
        visited[nx][ny] = 1   # 방문처리
        x = nx
        y = ny
        turn_count = 0   # 돌은 횟수 초기화
        count += 1   # 방문한 칸 수 추가
        continue
    else:
        turn_count += 1

    if turn_count == 4:   # 동서남북 다 확인했는데 못가는 경우
        nx = x - dx[d]
        ny = y - dy[d]

        if matrix[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break

        turn_count = 0


print(count)
