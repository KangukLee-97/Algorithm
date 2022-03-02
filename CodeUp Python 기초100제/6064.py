"""
6064: [기초-3항연산] 정수 3개 입력받아 가장 작은 값 출력하기
문제 Link: https://codeup.kr/problem.php?id=6064

Python으로 간단하게 표현해보기!
"""
# (1) 리스트에 저장하는 방법 -> 이 방법도 가능한 것 같은데 왜 이런 방법을 안쓸까?
s = list(map(int, input().split()))   # 3개 정수 입력받기
print(min(s))

# (2) 리스트 컴프리헨션으로 해결
a, b, c = map(int, input().split())
print((a if a < b else b) if ((a if a < b else b) < c) else c)