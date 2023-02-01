'''
Chapter02-2
파이썬 완전 기초
파이썬 함수
'''


# 기본 선언 

n = 700

print()

# 출력
print(n)
print(type(n))          # n의 자료형을 보여줌, <class 'int'>는 n이 정수형이라고 알려주는거임

# 동시선언
x = y = z = 700
print(x, y, z)


print()

# 선언
var = 75

# 재선언
var = "Change Value"

# 출력
print(var)
print(type(var))            # 마지막에 선언된 값이 기존의 것을 재할당

# Object References
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

print()

# 예1)
print(300)
print(int(300))     

print()

# 예2)
# n -> 777
n = 777
print(n, type(n))

m = n
print(m, type(m))

m = 400
print(m, n)

print()

# id(identity)확인 : 객체의 고유값 확인

m = 800 
n = 655

print(id(m))
print(id(n))
print(id(m) == id(n))           # id(m) 과 id(n)이 같냐, ==는 같냐고 물어보는거임

m = 800
n = 800
print(id(m))
print(id(n))
print(id(m) == id(n))           # true 라고 나옴

print()

# 다양한 변수 선언
# Camel Case : number0fCollegeGraduates -> Method             # 처음에는 소문자로 시작하고 연결되는 단어의 첫 글자를 대문자로 시작
# Pascal Case : NumberOfColleageGraduates -> Class            # 처음 대문자 연결되는 단어 다 대문자 시작
# Snake Case : number_of_colleage_graduates                   # 다 소문자에 _로 연결, 파이썬에서 변수선언할때 많이 사용


# 허용하는 변수 선언 법         # 숫자시작은 안됨
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8

# 예약어는 변수명으로 불가능
"""
False	def	if	raise
None	del	import	return
True	elif	in	try
and	else	is	while
as	except	lambda	with
assert	finally	nonlocal	yield
break	for	not	
class	from	or	
continue	global	pass	
"""