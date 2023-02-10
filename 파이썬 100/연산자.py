# 파이썬 프로그래밍 언어에서 연산자의 종류와 쓰임을 말해보시오.
# 자주쓰는 연산자 위주로 말해보시오.

# [1] : 산술 연산자
#   +,   -,   /,   // : 몫 구하기,  ** : 제곱,    % : 나머지 구하기
# 정수형끼리의 연산 --> 정수형
# 실수형끼리의 연산 --> 실수형
# 정수형과 실수형의 연산 --> 실수형

# [2] : 관계 연산자
# 대소비교를 하거나 같은지 같지 않은지 등의 비교를 할 때 사용한다.
#   >,  <,  >=,  <=, ==, !=(같지않다)

# [3] : 논리 연산자
# and, or, not
# and : 양쪽 값이 모두 참인 경우에만 참.
# or : 어느 한쪽만 참이면 참
# not : 참이면 거짓, 거짓이면 참

# [4] : 부울(Boolean) 연산자
# True, False 값으로 출력.


# 산술 연산자 예제를 만들어보시오.

# [1] : 산술 연산자
print(10+10)
print(10-5)
print(10*10)
print(10/10)    # 1.0(float)
print(3 ** 2)
print(10//3)    # 몫
print(10%3)     # 나머지


# 관계 연산자 예제를 만들어보시오.

# [1]: 관계연산자
print(10>5)     # True, False로 출력
print(10<5)
print('-'*140)
print(1 == 1)   # 같냐 -> True
print(1 != 2)   # 같지않냐 -> True
print(1 != 1)


print()


# 논리 연산자 예제를 만들어보시오.

# [1] : 논리연산자
a = True
b = False

print(a and b)
print(a or b)
print(a, not(a))

if a or b:
    print('True')
else:
    print('False')


print()


# 할당 연산자 예제를 만들어보시오.

# [1] : 할당 연산자
a = 100
a = a + 1
print(a)

b = 200
b += 1
print(b)


print()

# 멤버쉽 연산자(in) 예제를 만들어보시오.

# [1] : in 연산자
lst = [1, 2, 3, 4, 5]
print(lst, type(lst))

a = 5 in lst
print(a)

tpl = 1, 2, 3
print(tpl, type(tpl))


print()


# 부울 연산자 예제를 만들어 보시오.

# [1] : 부울 연산자 --> True, False 결과 반환
print(bool(1))      # 1은 참을 의미
print(bool(0))      # 0은 거짓 의미
print(bool(-1))     # 참
print(bool(None))   # None 값은 거짓

# [2] : None
print(type(None))

