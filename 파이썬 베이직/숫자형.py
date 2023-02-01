# Chapter 03-1
# 숫자형

# 파이썬 지원 자료형
'''
int : 정수
float : tlftn
complex : 복소수
bool : 불린
str : 문자열(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전
'''

# 데이터 타입
str1 = "Python"
bool = True
str2 = 'Anaconda'
float_v = 10.0            # 10과 10.0은 다름 
int_v = 7
list = [str1, str2]             

print(list)
dict = {   
    "name": "Machine Learning",             # 앞의것을 키라고 함(name, version)
    "version": 2.0
}
tuple = (7, 8, 9)
set = {3, 5, 7}



# 데이터 타입 
# 출력
print(type(str1))
print(type(bool))
print(type(str2))
print(type(float_v))
print(type(int_v))
print(type(dict))
print(type(tuple))
print(type(set))

print()

# 숫자형 연산자
"""
+
-
*
/
// : 몫만 반환
% : 나머지만 반환
abs(x) : 절대값
pow(x, y) : x의 y제곱 
= x**y
"""

# 정수 선언
i = 77
i2 = -14
big_int = 7777777777777777777777999999999999999999

print()

# 정수 출력
print(i)
print(i2)
print(big_int)

print()

# 실수 출력
f = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3 / 9

print(f)
print(f2)
print(f3)
print(f4)

print()

# 연산 실습
i1 = 39
i2 = 939
big_int1 =7777777777777777777777777779999999999999999999
big_int2 = 213128782159837187923253285823758723829849184
f1 = 1.234
f2 = 3.939

# +
print(">>>>> +")
print("i1 + i2 : ", i1 + i2)
print("f1 + f2 : ", f1 + f2)
print("big_int1 + big_int2 : ", big_int1 + big_int2)

print()

a = 3+1.0
print(a)
print(type(a))          # 서로 다른 것들을 연산하면 자동으로 형 변환이 이루어진다.

# *
print(">>>>> *")
print("i1 * i2 : ", i1 * i2)
print("f1 * f2 : ", f1 * f2)
print("big_int1 * big_int2 : ", big_int1 * big_int2)

print()

# 형 변환 실습
a = 3.          # 3.0을 의미
b = 6
c = .7          # 0.7을 의미
d = 12.7

# 타입 출력
print(type(a), type(b), type(c), type(d))

print()

# 형 변환
print(float(b))             # 6.0으로 형 변환
print(int(c))               # 0.7의 정수부분 0
print(int(d))               # 12.7의 정수부분 12
print(int(True))            # True : 1, False : 0 규칙임
print(float(False))         # 원래 거짓은 0인데 float이라 0.0
print(complex('3'))         # 복소수로 변환
print(complex('3'))         # 파이썬에서는 문자형을 숫자형으로 변환 후 복소수로 변환

print()

# 수치 연산 함수
print(abs(-7))
x, y = divmod(100, 8)       # 100을 8로 나누었을때 몫을 x, 나머지를 y

print(x, y)
print(pow(5,3), 5**3)

print()

# 외부 모듈
import math

print(math.pi)
print(math.ceil(5.1))       # x 이상의 수 중에서 가장 작은 정수(5.1보다 큰 정수)

# 실습
print('%1.4f' % math.pi)
print('%0.6f' % math.pi)
print('{:0.6f}'.format(math.pi))