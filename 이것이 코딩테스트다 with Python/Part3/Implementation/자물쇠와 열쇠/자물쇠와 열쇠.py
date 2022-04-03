"""
2020년도 카카오 신입 공채 문제
https://programmers.co.kr/learn/courses/30/lessons/60059
"""

n, m = map(int, input().split())   # n은 자물쇠 크기, m은 key 크기
key = []
lock = []

# key와 lock 2차원 배열 data 채워넣기
for i in range(n):
    lock.append(list(map(int, input().split())))
for i in range(m):
    key.append(list(map(int, input().split())))


# 2차원 리스트 90도 회전 (암기 필수!)
def rotate_key(key):
    n = len(key)  # 세로 크기
    m = len(key[0])   # 가로 크기
    result = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = key[i][j]

    return result


def check(new_lock, start, end):
    for i in range(start, end):
        for j in range(start, end):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    start = len(key) - 1   # lock의 시작지점, key와 최소 1개는 겹쳐야 하기 때문
    end = start + len(lock)   # lock이 끝나는 지점
    size = len(lock) + start * 2   # lock 확장 사이즈
    new_lock = [[0] * size for _ in range(size)]

    # 확장한 lock의 중앙 부분에 기존 lock을 위치
    for i in range(len(lock)):
        for j in range(len(lock)):
            new_lock[start + i][start + j] = lock[i][j]

    for _ in range(4):
        key = rotate_key(key)   # key 회전
        for r in range(end):
            for c in range(end):
                # 자물쇠에 열쇠 넣기
                for i in range(len(key)):
                    for j in range(len(key)):
                        new_lock[r + i][c + j] += key[i][j]
                # 열쇠가 정확히 맞는지 검사
                if check(new_lock, start, end) == True:
                    return True
                else:   # 안맞으면 다시 빼야함
                    for i in range(len(key)):
                        for j in range(len(key)):
                            new_lock[r + i][c + j] -= key[i][j]
    return False


print(solution(key, lock))
