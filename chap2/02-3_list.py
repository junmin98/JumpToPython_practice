# 1. 리스트 연산하기
# 더하기
a = [1, 2, 3]
b = [4, 5, 6]
print(a+b) # [1, 2, 3, 4, 5, 6]

# 반복하기
print(a*3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# 2. 리스트의 수정과 삭제
a[2] = 4 # 값 수정
print(a) # [1, 2, 4]

del a[1] # 리스트 요소 삭제
print(a) # [1, 4]

# 3. 리스트 관련 함수들
# .append() : 리스트에 요소 추가. 어떤 자료형도 추가 가능
# .sort()   : 리스트의 요소를 순서대로 정렬
# .reverse(): 리스트를 역순으로 뒤집어준다. (현재의 리스트를 그대로 거꾸로 뒤집음)
# .index(x) : 리스트에 x 값이 있으면 x의 인덱스 값을 리턴 
# .insert(a, b) : a번째 위치에 b를 삽입
a = [1, 2, 3]
a.insert(0, 4)
print(a) # [4, 1, 2, 3]
# .remove(x)    : 리스트에서 첫 번째로 나오는 x를 삭제
# .pop()    : 리스트의 맨 마지막 요소 리턴 후, 해당 요소 삭제
a.pop()
print(a) # [4, 1, 2]
# .pop(x)   : x번째 요소 리턴 후, 삭제
# .count(x) : 리스트 안에 x가 몇 개 있는지 조사하여, 그 개수 리턴
a = [1, 2, 3, 1]
print(a.count(1))
# .extend(x)    : x에는 리스트만 올 수 있으며 원래의 a 리스트에 x 리스트를 더함
a = [1, 2, 3]
a.extend([4, 5])
print(a)
b = [6, 7]
a.extend(b)
print(a)
# a.extend([4, 5])는 a+=[4,5]와 동일하다. 
