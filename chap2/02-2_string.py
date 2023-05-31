# 포맷 코드와 숫자 함께 사용하기

# 1. 정렬과 공백
print("%10s" % "hi") # %10s: 전체 길이가 10개인 문자열 공간에서 대입되는 값을 오른쪽 정렬하고, 그 앞의 나머지는 공백으로 남겨두라는 의미
print("%-10sjane" % "hi")

# 2. 소수점 표현하기
print("%0.4f" % 3.42123123) # 소수점 네 번째 자리까지만 표현

# 3. format 함수를 사용한 포맷팅
number = 10
day = "three"
print("I eat {0} apples. so I was sick for {1} days".format(number, day))

# 정렬: 왼쪽 정렬 (:<10), 오른쪽 정렬 (:>10), 가운데 정렬 (:^10)
# 공백 채우기
print("{0:=^20}".format("hi"))

# 4. f 문자열 포매팅
name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')