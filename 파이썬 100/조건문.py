# 파이썬 프로그래밍 언어에서의 기본적인 if 조건문 예제를 구현한 것이다.
# 아래 if문중 틀린 것을 찾으시오

# [!] : 조건문
# 대부분의 프로그래밍 언어가 그러하듯이 파이썬에서도 조건문은 if문을 사용한다.
# 다른 언어와 파이썬의 차이점 --> if문 끝에 콜론(:)을 붙여서 if문 줄 (line)의 끝을 알려줘야 한다.

a = 100
# [1]
if a <= 100:
    print(a)

# [2]
if a <= 100:
    print(a)

# [3]
if a <= 100             :           # 이렇게 쓰는사람은 없지만 에러 안남
    print(a)

# [4]
if a <= 100: print(a)               #

#[5]
# if a<= 100: print(a):     # 프린트문 뒤에도 붙여서 에러

# [6]
# if a <= 100; print(a)     # 새미콜론이라 에러

print('--'*50)

# 파이썬의 기본적인 if ... else 조건문과 if .. elif..else 조건문 예제를 구현하시오.

# [1] : if..else 조건문
a = 120

if a > 120:
    print('a는 120보다 크다.')
else:
    print('a는 120보다 작다.')

# [2] : if..elif..else 조건문
age = 28
if age < 30:
    print('청년')
elif age < 60:
    print('중년')
else:
    print('노년')

print('--'*50)

# 아래는 한 카페의 메뉴 선택기를 if 조건문으로 구현한 것인데 틀린곳을 찾아보시오.
# 커피숍의 메뉴는 1번 아메리카노, 2번 카페라떼, 3번 아이스카페라떼

# [1] : 카페메뉴 선택기
btn = 1

if btn == 1:                # if btn = 1: -> =는 할당하는 것이기 때문에 ==로 사용
    print('아메리카노')
elif btn == 2:
    print('카페라떼')
elif btn == 3:
    print('아이스 카페라떼')
else:
    print('메뉴는 1, 2, 3 번중 하나를 골라주세요')


print('--'*50)

# 아래의 조건문에서 else문의 위치에 따라 에러가 나는 것을 말해보시오.

# [1] : 카페 메뉴 선택기
btn = 3
if btn == 1:
    print('아메리카노')
# else:                                             # else문이 중간에 들어오면 에러
#     print('메뉴는 1,2,3번중 하나를 골라주세요!')
elif btn == 2:
    print('카페라떼')
elif btn == 3:
    print('아이스 카페라떼')

# [2] : 카페 메뉴 선택기
btn = 3
if btn == 1:
    print('아메리카노')
elif btn == 2:
    print('카페라떼')
elif btn == 3:
    print('아이스 카페라떼')
