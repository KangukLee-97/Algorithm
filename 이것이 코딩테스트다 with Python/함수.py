"""
 처음보는 함수 선언법?
"""
def printMessage(a, b):
    print("a: {}".format(a))
    print("b: {}".format(b))


printMessage(b="안녕", a="너는")

"""
 global?
  - 함수 안에서 함수 밖의 변수 데이터를 변경해야 하는 경우에 사용한다. 
  - global 키워드로 변수를 지정하면 해당 함수에서는 지역 변수를 만들지 않고 함수 바깥에 선언된 변수를 바로 참조하게 된다.
"""
a = 0

def func():
    global a
    a += 1

for i in range(10):
    func()

print(a)

"""
 람다 표현식
  - 특정한 기능을 수행하는 함수를 한 줄에 작성할 수 있다는 점이 장점이다. 
  - 간단한 기능의 함수는 람다 표현식을 사용하면 좋다.
"""
def add(a, b):
    return a + b

# 일반적인 add() 메서드 사용
print(add(3, 7))

# 람다 표현식으로 구현한 add() 메서드
print((lambda i, j: i + j)(3, 7))