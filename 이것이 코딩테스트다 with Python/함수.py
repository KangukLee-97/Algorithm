"""
 처음보는 함수 선언법?
"""
def printMessage(a, b):
    print("a: {}".format(a))
    print("b: {}".format(b))


printMessage(b="안녕", a="너는")

"""
 global?
  - 함수 내에서는 지역변수를 만들지 않고 함수 바깥에 선언된 변수를 참조하게 된다.
  - 단순히 함수 바깥의 변수를 사용하는 것은 오류가 없지만, 값을 수정할 때는 global 키워드로 변수를 지정해야 한다.
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