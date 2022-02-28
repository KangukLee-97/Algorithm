"""
6059~6062: [기초-비트단위논리연산] 비트단위로 NOT/AND/OR/XOR 하여 출력하기
문제 Link: https://codeup.kr/problem.php?id=6059

NOT: ~, AND: &, OR: |, XOR: ^
"""
a = int(input())
print(~a)

x, y = map(int, input().split())
print(x & y)
print(x | y)
print(x ^ y)