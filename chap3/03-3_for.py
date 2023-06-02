# 다양한 for문의 사용
a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first + last)

# for문의 응용
marks = [90, 25, 67, 45, 80]
for i, mark in enumerate(marks):
    if mark >= 60:
        print(f"{i+1}번 학생은 합격입니다.")
    else:
        print(f"{i+1}번 학생은 불합격입니다.")