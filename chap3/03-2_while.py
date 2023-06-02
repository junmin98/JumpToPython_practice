# while문 강제로 빠져나가기: coffee.py
coffee = 10
while True:
    money = int(input("돈을 넣어주세요: "))
    if money == 300:
        print("커피를 줍니다")
        coffee -= 1

    elif money > 300:
        print(f"거스름돈 {money-300}를 주고 커피를 줍니다.")
        coffee -=1

    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print(f"남은 커피의 양은 {coffee}개 입니다.")
    
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

# while문의 맨 처음으로 돌아가기
a = 0
while a < 10:
    a += 1
    if a % 2 == 0: continue
    print(a)