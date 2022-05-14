n = int(input())   # 보드의 크기
k = int(input())   # 사과의 개수
board = [[0] * (n+1) for _ in range(n+1)]   # (N+1) X (N+1) 보드 생성
move_info = []   # 뱀의 방향 변환 정보 리스트

for _ in range(k):
    ax, ay = map(int, input().split())   # 사과의 좌표 x,y
    board[ax][ay] = 1   # board에 사과 위치 1로 설정

l = int(input())   # 뱀의 방향 변환 횟수
for i in range(l):
    x, c = input().split()
    move_info.append((int(x), c))


# 동 -> 남 -> 서 -> 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def turn(direction, c):
    if c == "L":   # 왼쪽으로 90도 회전이라면
        return (direction + 3) % 4
    else:   # 오른쪽으로 90도 회전이라면
        return (direction + 1) % 4


def solution():
    x, y = 1, 1   # 뱀 시작 위치
    board[x][y] = 2   # 자기 자신의 몸과 부딛힌 경우는 2
    direction = 0   # 뱀이 바라보고 있는 방향
    second = 0   # 경과한 시간
    info_idx = 0   # 방향 변환 정보 리스트 인덱스
    q = [(x, y)]

    while True:
        # 이동한 좌표
        nx = x + dx[direction]
        ny = y + dy[direction]
        if nx >= 1 and nx <= n and ny >= 1 and ny <= n and board[nx][ny] != 2:
            if board[nx][ny] == 0:   # 사과가 없다면
                board[nx][ny] = 2
            else:   # 사과가 있다면
                pass
        else:
            second += 1
            break
