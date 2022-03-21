n = int(input())   # 공간의 크기
plan = list(input().split())   # 계획서 내용
x, y = 1, 1   # 현재 위치는 1,1

dx = [0, -1, 0, 1]   # 동, 북, 서, 남
dy = [1, 0, -1, 0]   # 동, 북, 서, 남
move_types = ['R', 'U', 'L', 'D']

for p in plan:
    for i in range(len(move_types)):
        if p == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue

        x, y = nx, ny

print(x, y)
