t1 = ()
t2 = (1, ) # 1개의 요소만 가질 때 요소 뒤에 콤마 반드시 붙여야 함
t3 = (1, 2, 3)
t4 = 1, 2, 3 # 괄호 생략 가능
t5 = ('a', 'b', ('ab', 'cd'))

# 튜플 다루기
# 튜플 더하기
t1 = (1, 2, 'a', 'b')
t2 = (3, 4)
t3 = t1 + t2 # t1과 t2의 요솟값이 바뀌는 것이 아니라, 둘을 더하여 새로운 튜플 t3를 생성
print(t3)

# 튜플 곱하기
t3 = t2 * 3
print(t3)