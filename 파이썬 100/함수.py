# 파이썬의 기본적인 함수 작성과 호출에 대한 코드를 구현하시오.
# 함수 이름은 a(), b() 라고 한다.

# [1] : 함수작성
def a():
    print('붕어빵')

def b():
    print('개구리빵')

# [2] : 함수 호출
a()
b()

print('-'*100)

# 리턴값이 있는 함수를 작성하시오.
# 앞서 리턴값이 없는 기본 함수를 가지고 리턴값이 있도록 수정하여 구현하시오.

# [1]
def a():
    result = '붕어빵'
    return result


# [2]
print(a())

print('-'*100)

# 변수의 메모리 주소값을 출력하여 다른 함수내 같은 변수의 값들이 어떤 주소를 가지고 있는지 출력하시오

# [1] : 함수작성
def a():
    result = '붕어빵'
    result_loc = id(result)
    return result_loc


def b():
    result = '개구리빵'
    result_loc = id(result)
    return result_loc

# [2] : 함수호출
print(a())
print(b())

print('-'*100)

# 한 반의 학생들 10명에 대한 영어 점수표가 리스트로 있다.
# 최고 점수를 출력하는 함수를 만들어 영어 점수표를 함수로 전달하면 최고 점수가 나오도록 구현해보시오.
# (응용) 최저 점수가 나오도록 수정해보시오.

# [1] : 함수작성
def max_in_list(lst):
    return max(lst)         # max() 함수는 전달받은 리스트내 요소중 가장 큰 숫자를 반환 <-> min()

# [2] : 영어 점수표
english_score=[35,55,87,98,48,88,77,65,91]

# [3] : 함수 호출 및 결과 출력하기
result = max_in_list(english_score)
print(result)

print('-'*100)

# 한 반의 학생들 10명에 대한 영어 점수표가 리스트로 있다.
# 함수를 만들어 영어 점수표를 함수로 전달하면 최고 점수와 최저 점수가 동시에 나오도록 구현해본 것이다.
# (문제1) 아래 코드의 결과를 말해보시오. 
# (문제2) 만약 예상한 결과가 출력되지 않았다면 왜 그런지 이유를 말해보시오.

# [1]
def max_min_list(lst):
    return max(lst),min(lst)                 
    
# [2] : 영어 점수표
english_score = [35,90,58,30,98,56,89,78,91,67]

# [3] : 함수 호출 및 결과 출력하기
result = max_min_list(english_score)
print(result,type(result))       # 튜플로 반환

# [4] : a,b 변수 각각에 최고, 최저 점수를 받아서 출력하기
a, b = max_min_list(english_score)
print(a)
print(b)

print('-'*100)


# 오름차순, 내림차순 정렬을 sort(), sorted() 함수로 구현하시오.
# sort(), sorted() 함수의 차이점을 아는지 묻는 문제이다.

# [1] : 리스트
lst = [100,40,70,90,60]

# [2] : sort()함수를 이용한 오름차순, 내림차순 정렬
lst = [100,40,70,90,60]
lst.sort()             # 오름차순
print(lst)

lst = [100,40,70,90,60]
lst.sort(reverse=True) # 내림차순
print(lst)

# [3] : sorted()
lst = [100,40,70,90,60]
lst = sorted(lst)
print(lst)

# [4] : sorted() --> 내림차순
lst = [100,40,70,90,60]
lst = sorted(lst, reverse=True)
print(lst)

print('-'*100)

# 함수 호출시 입력 파라미터 값을 지정하여 함수를 호출하는 예제를 만들어 보시오.

# [1] : 함수 호출시 입력 파라미터 지정
def my_func(id_,name_, strength_):
    return id_, name_, strength_

result = my_func(id_='batman', name_='베트맨', strength_='900')
print(result,type(result))

print('-'*100)

# 아래 코드의 결과를 말해보고 타입은 무엇으로 나오는지 설명해보시오.
# 이 문제는 함수에서 리턴되는 값에 대해서 한개 또는 여러 개의 리턴 값이 어떻게 처리되는지를 아는지 묻는 문제이다.

def my_func( id_, name_, power ):
    return id_, name_, power

result = my_func( id_='superman', name_='슈퍼맨', power=3000 )
a, b, c = my_func( id_='batman', name_='배트맨', power=4000 )

print(result, type(result))
print(result[2],type(result[2]))

print(a,type(a),b,type(b),c,type(c))

print('-'*100)

# 파이썬 함수에서 디폴트 파라미터란 무엇인지 설명하고 부가세 계산 프로그램을 만들어보시오.
# 이때 공급가 구하는 부분을 디폴트 파라미터로 받아 구현하시오.

# [1] : 부가세 계산하기

def calc_tax(price, operator=1.1):
    supply_value = round(price/operator)
    vat = price - supply_value
    total = (price/operator)*operator
    return supply_value, vat, int(total)

result = calc_tax(110000)
print(result)

print('-'*100)

# [!] : 내 응용!!

# a = int(input('금액 말해라 : '))
# def calc_tax(price, operator=1.1):
#     supply_value = round(price/operator)
#     vat = price - supply_value
#     total = (price/operator)*operator
#     return supply_value, vat, int(total)

# result = calc_tax(a)
# print('공급가는', result[0],'입니다.')
# print('부가세는', result[1],'입니다.')
# print('두개 더해서 가격이', result[2],'입니다.')


# 함수 호출시 파라미터 갯수를 알 수 없는 상황에서는 함수를 어떻게 만들어야하는지 예제로 설명하시오.
# 이 문제는 가변길이 인수 목록을 어떻게 받는지를 아는지 묻는 문제이다.

# [1] : 가변길이 입력 파라미터 --> 함수에서 입력파라미터를 받을때 * 표시를 해줌으로써 가변길이라는 것을 명시적으로 표시
def my_func(*params):
    n=0
    for i in params:
        n += i
    return n

a = my_func(1,1,1,1)
print(a)

b = my_func(1,2,3,4,5,6,7,8,9)
print(b)

print('-'*100)


# 가변길이 입력 파라미터 값을 함수가 받았을 때 그때의 자료형은 무엇인가?
# 이 문제는 가변길이 인수 목록이 전달되면 그 값이 무엇이고 반복 가능한 객체인지를 알고 있는지 묻는 문제이다.

def my_func(*params):
    n = params
    return n,type(n)

a=my_func(1,1,1,1)
print(a)

# 가변길이 입력 파라미터 값들을 함수로 넘겨서 해당 파라미터의 갯수와 홀수들의 합을 구하는 코드를 구현하시오.
# 함수의 리턴은 항상 하나의 값을 반환한다. 
# 아래 코드의 결과로 출력되는 자료형에 대해서 말해보시오.

def my_func(*params):
    count_=0
    sum_=0
    for i in params:
        count_ += 1
        if i % 2 != 0:
            sum_+=i
    return count_, sum_
a,b = my_func(1,2,3,4,5,6,7,8,9,10)
result = my_func(1,2,3,4,5,6,7,8,9,10,11)

print(a,b, type(a))