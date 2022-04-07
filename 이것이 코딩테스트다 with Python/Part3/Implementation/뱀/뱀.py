n = int(input())   # 보드의 크기
k = int(input())   # 사과의 개수
board = [[0] * n for _ in range(n)]   # N X N 보드 생성
move_info = []   # 뱀의 방향 변환 정보 리스트

for i in range(k):
    ax, ay = map(int, input().split())   # 사과의 좌표 x,y
    board[ax][ay] = 1   # board에 사과 위치 1로 설정

l = int(input())   # 뱀의 방향 변환 횟수
for i in range(l):
    info = list(map(str, input().split()))
    info[0] = int(info[0])
    move_info.append(info)
