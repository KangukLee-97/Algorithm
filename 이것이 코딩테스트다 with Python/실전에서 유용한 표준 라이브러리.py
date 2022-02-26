"""
 내장함수: 기본 입출력 함수부터 정렬함수까지 기본적인 함수제공
    - sum(), min(), max(), eval(), sorted()
      => eval(): 사람의 입장에서 작성된 수식만 가능
      => sorted(): key 속성으로 정렬 가능. 주로 lambda 사용함.
"""
"""
 itertools: 반복되는 형태의 데이터를 처리하기 위한 유용한 기능 제공
  - 순열과 조합은 완전탐색 유형에서 자주 사용된다. 
    => 순열: 서로 다른 n개에서 서로 다른 r개를 선택해서 일렬로 나열함 (순서고려함)
    => 조합: 서로 다른 n개에서 순서 상관없이 서로 다른 r개를 선택함 (순서고려안함)
"""
# <itertools: 순열과 조합>
from itertools import permutations, combinations, product, combinations_with_replacement

data = ['A', 'B', 'C']
result_p = list(permutations(data, 3))   # 3P3
print(result_p)
result_c = list(combinations(data, 2))   # 3C2
print(result_c)
# 중복 순열,조합
result_rp = list(product(data, repeat=2))   # 2개를 뽑는 모든 순열 구하기 (중복 허용)
print(result_rp)
result_rc = list(combinations_with_replacement(data, 2))   # 2개를 뽑는 모든 조합 구하기 (중복 허용)
print(result_rc)

"""
 collections: deque, counter 등 유용한 자료구조를 포함한다.
  - counter: 리스트와 같은 반복가능한 객체가 주어졌을 때 내부의 원소가 몇 번씩 등장했는지 알려준다.
"""
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(counter['blue'])   # blue가 등장한 횟수
print(counter['green'])
print(dict(counter))

"""
 math: 필수적인 수학적 기능 제공
    -  팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 함수부터 파이(pi)와 같은 상수를 포함
"""