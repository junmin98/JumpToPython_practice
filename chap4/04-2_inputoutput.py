# 한 줄에 결괏값 출력하기

# for i in range(10):
#     print(i, end=' ') # end 매개변수의 초깃값은 줄바꿈(\n)문자이다.


# 프로그램의 입력과 출력
import sys
args = sys.argv[1:]
for i in args:
    print(i.upper(), end = ' ')