"""
 궁금한 점)
  현재 내 풀이는 책에서의 풀이와는 약간 다른 형태로 구현했다.
  내가 구현한대로 풀이를 해도 괜찮을지...?
"""
n = int(input())
person = sorted(list(map(int, input().split())), reverse=True)
result = 0
cur = 0

while cur < len(person):
    cur += person[cur]
    result += 1

print(result)