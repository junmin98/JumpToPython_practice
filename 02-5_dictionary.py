# 1. 딕셔너리에 쌍 추가, 삭제하기
# - 쌍 추가하기
a = {1: 'a'}
a[3] = 'b'
print(a) # {1: 'a', 3: 'b'}

# - 딕셔너리 요소 삭제하기: del a[key]
del a[1]
print(a)

# 2. 딕셔너리 관련 함수들
# - key 리스트 만들기 (key)
a = {'name': 'junmin', 'phone':'010-2823-3765', 'birth':'0821'}
print(a.keys()) # dict_keys --> 기본적인 반복구문에서 사용 가능
for k in a.keys():
    print(k)

print(list(a.keys())) # --> dict_keys 객체를 리스트로 변환
# - value 리스트 만들기
print(a.values())
# - key, value 쌍 얻기 (items)
print(a.items()) # items 함수는 key와 value의 쌍을 튜플로 묶은 값을 dict_itmes 객체로 돌려준다.
# - key: value 쌍 모두 지우기 (clear)
print(a.clear())
# - key로 value 얻기 (get)
a = {'name': 'junmin', 'phone':'010-2823-3765', 'birth':'0821'}
print(a.get('name'))
# - 해당 key가 딕셔너리 안에 있는지 조사하기 (in)
print('name' in a)