# Chapter 04-1
# 파이썬 제어문
# If 실습

# 기본형식
print(type(True))           # 0 이 아닌 수, "abc", [1, 2, 3..], (1,2,3...) ...
print(type(False))          # 0, "", [], (), {}, ..., 비어있는 느낌

print()

# 예1

if True:
    print('Good')          # 들여쓰기 안하면 에러남

if False:
    print('Bad')

# 예 2
if False:
    print('Bad!')
else:                       # if의 첫번째것이 실행이 되지 않는다면 뒤에 그밖에는 실행이 됨
    print('Good!')

if True:
    print('Bad!')
else:
    print('Good!')          # 앞에서 실행되었기 때문에 실행 안됨


print()


# 관계 연산자
# >, >=, <, <=, ==, !=
x = 15
y = 10

# 양변이 같을때 참
print(x == y)

# 양변이 다를때 참
print(x != y)

# 왼쪽이 클때 참
print(x > y)

# 왼쪽이 크거나 같을때 참
print(x >= y)

# 오른쪽이 클때 참
print(x < y)

# 오른쪽이 크거나 같을때 참
print(x <= y)

print()

# 예3
city=""
if city:
    print("You are in:", city)
else:
    print("Please enter your city")

# 예4
city2="Seoul"
if city2:
    print("You are in:", city)
else:
    print("Please enter your city")


# 논리연산자(중요)
# and, or, not

a = 75
b = 40
c = 10

print('and :', a > b and b > c) # a > b > c
print('or : ', a > b or b > c) 
print('not : ', not a > b)
print('not : ', not b > c)
print(not True)
print(not False)

# 산술, 관계, 논리 우선순위
# 산수 > 관계 > 논리 순서로 실행
print('e1 : ', 3+12 > 7+3)
print('e2 : ', 5 + 10 * 3 > 7 + 3 * 20)
print('e3 : ', 5 + 10 > 3 and 7 + 3 == 10)
print('e4 : ', 5 + 10 > 0 and not 7 + 3 == 10)


print()


# 예5
score1 = 90
score2 = 'A'

# 복수의 조건이 모두 참일 경우에 실행
if score1 >= 90 and score2 == 'A':
    print('Pass')
else:
    print('Fail')


print()


# 예6
id1 = 'vip'
id2 = 'admin'
grade = 'platinum'

if id1 == 'vip' or id2 == 'admin':
    print('관리자 입장')

if id2 == 'admin' and grade == 'platinum':
    print('최상위 관리자')


print()


# 에7

num = 90

if num >= 90:
    print('Grade : A')
elif num >= 80:
    print('Grade : B')
elif num >= 70:
    print('Grade : C')
else:
    print('과락')


print()


# 중첩 조건문(if 안에 if)

grade = 'A'
total = 88

if grade == 'A':
    if total >= 90:
        print('장학금 100%')
    elif total >= 80:
        print('장학금 80%')
    else:
        print('장학금 50%')
else:
    print('장학금 없음')


print()


# in, not in

q = [10, 20, 30]
w = {70, 80, 90, 100}
e = {"name": "Oh", "city": "Daejeon", "grade": "A"}
r = (10, 12, 14)

print(15 in q)
print(90 in w)
print(12 not in r)
print("name" in e)
print("Daejeon" in e.values())          # "Daejeon"은 키가 아니라 값이기 때문에 values로 값이 있는지 확인