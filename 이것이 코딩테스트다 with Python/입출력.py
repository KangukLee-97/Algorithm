"""
 입력
  - input(): 한 줄의 문자열을 입력받을 때 사용하는 함수
  - 여러 개의 데이터를 입력받을 때는 보통 데이터가 공백으로 구분되는 경우가 많다!
    => map을 사용한다! (map(): 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용한다)
    => list(map(int, input().split())

  - 하지만, 데이터의 개수가 많지 않다면 단순히 map(int, input().split())을 사용해도 무방하다.

 빠르게 입력받아야 하는 경우
  - 흔히 정렬, 이진탐색, 최단경로 문제의 경우에는 매우 많은 수의 데이터가 연속적으로 입력됨.
  - sys 라이브러리에 정의되어 있는 sys.stdin.readline() 함수를 이용한다.
    => 하지만 readline()으로 입력 후 엔트가 줄 바꿈 기호로 입력되는데 이 기호를 제거하려면 rstrip()을 사용해야 한다.
    => ** sys.stdin.readline().rstrip() **
"""
# <단순 입력>
# n = int(input())   # 데이터 갯수 입력
# data = list(map(int, input().split()))   # 각 데이터를 공백으로 구분하여 입력
# data.sort(reverse=True)
# print(data)

# <빠르게 입력>
import sys

data = sys.stdin.readline().rstrip()
print(data)

"""
 출력
  - print(): 자동 줄바꿈, 
"""