# 매개변수와 인수
# 매개변수: 함수에 입력으로 전달된 값을 받는 변수
# 인수   : 함수를 호출할 때 전달하는 입력값

def add(a, b): # a, b --> 매개변수
    return a+b

print(add(3, 4)) # 3, 4는 인수

# 입력값이 몇 개가 될 지 모를 때
# def 함수이름(*매개변수):
#   <수행할 문장>

def add_many(*args):
    # args: (1, 2, 3, 4) - tuple
    result = 0
    for i in args:
        result += i
    return result

print(add_many(1, 2, 3, 4))

# 키워드 매개변수 kwargs: 매개변수 앞에 별 두개 (**)
def print_kwargs(**kwargs):
    # kwargs --> dictionary (key=value) 형태의 입력값이 딕셔너리에 저장됨
    print(kwargs)

print_kwargs(name='foo', age=3)

# return의 또 다른 쓰임새: 특별한 상황일 때 함수를 빠져나가고 싶다면 return을 단독으로 써서 함수를 즉시 빠져나감
def say_nick(nick):
    if nick == "바보":
        return
    print(f"nick의 별명은 {nick}입니다.")

say_nick("바보")

# 함수 안에서 함수 밖의 변수를 변경하는 방법
# (1) return 사용하기
a = 1
def vartest(a):
    a = a+1
    return a
a = vartest(a)
print(a)

# (2) global 사용하기
a = 1 
def vartest2():
    global a # 함수 안에서 함수 밖의 a 변수를 직접 사용하겠다.
    a = a+1
vartest2()
print(a)

# lambda
add = lambda a, b: a+b
print(add(3, 4))