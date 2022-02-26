"""
 리스트 자료형
  - 배열 (Array)
  - Method: append, sort, reverse, insert, count, remove
  - 리스트 컴프리헨션: []안에 조건문과 반복문을 넣어서 간결하게 리스트 초기화 가능
"""
# <리스트 컴프리헨션>
# ex) 0부터 19까지의 수 중에서 홀수만 포함하는 리스트를 출력
array = [i for i in range(20) if i % 2 == 1]
print(array)

# ex) 1부터 9까지 수의 제곱 값을 포함하는 리스트를 출력
array_two = [i*i for i in range(1, 10)]
print(array_two)

# ex) 2차원 리스트 초기화 (N X M)
n = 3
m = 4
array_three = [[0] * m for _ in range(n)]
print(array_three)

# <리스트 Method - remove>
# remove는 리스트 내에서 하나만 제거하지만 여러 개를 제거하고 싶다면?
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}   # 집합 자료형
result = [i for i in a if i not in remove_set]   # remove_set에 포함되지 않은 값만 저장함
print(result)

"""
 문자열 자료형
  - 문자열 연산이 가능하다
  - 특정 위치의 값은 가져올 수 있지만, 수정은 불가능함!
"""

"""
 튜플 자료형
  - 한번 선언된 값을 변경할 수 없음.
  - 그래프 알고리즘을 구현할 때 자주 사용된다. (ex. 우선순위 큐)
  
 장점으로는..?
  - 리스트보다 공간효율적이다.
  - 서로 다른 성질의 데이터를 묶어서 관리할 때 용이하다 => 최단경로 알고리즘 (비용, 노드번호)
  - 데이터의 나열을 해싱의 키 값으로 사용해야 할 때 => 튜플은 변경이 불가능하기 때문에 리스트와 다르게 키 값으로 사용 가능
  - 리스트보다 메모리를 효율적으로 사용해야 할 때 용이함
"""
data_tuple = (1, 2, 3, 4)
print(data_tuple[3])

"""
 사전 자료형
 - 키와 값의 쌍을 데이터로 가지는 자료형
 - 변경 불가능한 자료형을 키로 사용할 수 있다.
 - 해시 테이블을 이용하므로 데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리가능

 Method
 - 키 데이터만 뽑아서 리스트로 이용할 때: keys()
 - 값 데이터만 뽑아서 리스트로 이용할 때: values()
"""
data_dict = dict()
data_dict['사과'] = 'Apple'
data_dict['바나나'] = 'Banana'
data_dict['코코넛'] = 'Coconut'
print(data_dict)

data_dict2 = {
    '사과': 'Apple',
    '바나나': 'Banana',
    '코코넛': 'Coconut'
}
print(data_dict2)

if '사과' in data_dict:
    print("\'사과\'를 키로 가지는 데이터가 존재합니다.")

key_list = data_dict.keys()
print(key_list)
print(list(key_list))   # 보통 리스트형으로 변환시켜서 사용한다.

value_list = data_dict.values()
print(value_list)

for key in key_list:
    print(data_dict[key])

"""
 집합 자료형
  - 중복을 허용하지 않는다
  - 순서가 없다
  - 리스트 혹은 문자열을 이용하여 초기화 가능하다 (단, set() 함수 이용)
  - 데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리할 수 있다.
  - 연산이 가능하다 (합집합, 교집합, 차집합)
  
 Method
  - 1개 원소 추가: add
  - 2개 이상의 원소 추가: update (ex. update([1,2]))
  - 특정 원소 삭제: remove
"""
data_set = set([1, 2, 3, 3, 4, 5, 5])
print(data_set)
data_set = {1, 2, 3, 3, 4, 5, 5}
print(data_set)

# 집합 자료형 연산
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
print(a | b)
print(a & b)
print(a - b)

"""
 리스트와 튜플은 순서가 있기 때문에 indexing을 통해서 자료형의 값을 얻을 수 있다. (ex. a[1])
 하지만 사전 자료형과 집합 자료형은 순서가 없기 때문에 indexing이 불가능하다. 
    => 사전의 key 혹은 집합의 element를 이용해서 O(1)의 시간 복잡도로 조회한다.
"""