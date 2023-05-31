# 리스트 복사
a = [1, 2, 3]
b = a

# print(id(a))    # id: 변수가 가리키고 있는 객제의 주소 값 리턴
# print(id(b))
# print(a is b)   # is:  동일한 객체를 가리키고 있는지 판단

a[1] = 4
# print(a)
# print(b)

# a 변수의 값을 가져오면서 다른 주소를 가리키도록 하는 방법
# 1. [:]이용
a = [1, 2, 3]
b = a[:]
# print(id(a))
# print(id(b))

# 2. copy 모듈 이용
from copy import copy
a = [1, 2, 3]
b = copy(a)
# print(a is b) # False

# 변수를 만드는 여러가지 방법
a, b = ('python', 'life')
print(a) # python (str)
print(b) # life (str)

(a, b) = 'python', 'life'
