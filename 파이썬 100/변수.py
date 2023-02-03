# 파이썬 프로그래밍 언어에서 변수란 무엇인지 설명해보시오.
# 변수의 역할은 무엇인지 설명해 보시오

# [1] : 변수란 무엇인가?
# 변하는 수 --> 변수
# 코드를 작성하는 과정에서 여러 유형의 데이터 값을 많이 사용하는데 이때 데이터 값을 담는 바구니
# 변수에는 최조의 저장된 값이 다른 값으로 변할 수 있음

# [2] : 변수의 역할은 무엇인가?
# 변수는 프로그램 코드 작성시 여러가지 다양한 데이터 값을 효율적으로 저장하고 관리하기 위한 용도로 사용
# 프로그래밍 코딩 시 변수를 적절히 사용함으로써 코딩을 보다 효율적으로 빨리 짤 수 있게 됨
# 변수 없이도 코드를 작성할 수 있지만 변수를 사용함으로써 더욱 효율적으로 할 수 있음



# 파이썬 프로그래밍 언어에서 상수란 무엇인지 설명해보시오.

# [1] : 상수란 무엇인가?
# 항상 변하지 않는 수 --> 상수
# 코드를 작성하는 과정에서 오직 하나의 데이터 값을 많이 사용하는데 이런 데이터 값을 담는 바구니
# 상수에는 최조의 저장된 값만이 담겨질 수 있다.
# 항상 고정된 값 그데로 유지되는 것이 상수이다.
# 사용자가 임의로 바꾸거나 변경할 수 없는 사전에 미리 정의된 값을 가지는 것
# 숫자 상수, 문자 상수 등이 있다.



# 파이썬으로 파이 값과 중력가속도 값을 상수로 정의하시오.
# [1] : 상수 선언 및 값 할당
# 파이썬에서는 다른 언어에서처럼 const 키워드로 상수를 지정하는 문법이 없다.
PI = 3.14
GRAVITY = 9.8

# [2] : 변수를 상수처럼 사용
# 변수를 대문자로 선언하고 상수처럼 사용
print(PI)
print(GRAVITY)


print()


# 파이썬의 기본적인 변수 선언과 변수값 할당을 보여주는 코드를 구현하시오.

# [1] : 변수 선언 및 변수 값 할당
# 파이썬은 변수를 선언시 메모리 공간을 예약하기 위해 명시적으로 선언 할 필요가 없음.
# 따라서, 바로 변수명을 적어주고 값을 할당하면 자동으로 변수 선언 및 변수 값 할당이 이루어지게 됨
# 이때, = 기호를 사용하는데 '할당' 또는 오른쪽의 값을 왼쪽에 '대입'한다는 의미.
a = 100
b = 3.14
c = 'k'
d = 'Hello World'

# [2] : 출력
print('[결과출력]')
print('a 변수의 값은?', a)
print('b 변수의 값은?', b)
print('c 변수의 값은?', c)
print('d 변수의 값은?', d)
print(a, b, c, d)


print()


# 변수 값 할당 시 여러 변수에 동시에 한 개의 값을 할당하는 다중 할당 코드를 구현하시오.

# [1] : 다중할당
# 파이썬은 기본적으로 하나의 값을 여러개의 변수에 할당하여 저장시킬 수 있다.
a = b = c = d = e = 100

# [2] : 출력
print('[결과출력]')
print(a, b, c, d, e)


print()


# 아래는 변수 값 할당시 여러 변수에 동시에 한 개의 값을 할당하는 다중 할당 코드이다.
# 값이 100, 200 이렇게 주어졌을 때 결과를 예상하여 말해보시오?
# 그때의 type은 무엇인지도 말해보시오?

# [1] : 다중 할당
# 파이썬은 기본적으로 하나의 값을 여러 개의 변수에 할당하여 저장시킬 수 있다.
a = b = c = d = e = 100, 200

# [2] : 출력
# 튜플로 출력됨
# (100, 200)이 한쌍
print('[결과출력]')
print(a, b, c, d, e)
print(type(a))


print()


# 다중 할당시 여러 개의 값을 여러 개의 변수에 각각 저장시키는 코드를 한줄로 구현하시오.
# 여러 개의 값 --> 100, 3.14, k, korea
# 여러 개의 변수 --> a, b, c, d

# [1] : 다중 할당
a, b, c, d = 100, 3.14, 'k', 'korea'

# [2] : 출력
print('[결과출력]')
print('a, b, c, d변수의 값은?', a, b, c, d)


print()


# 아래와 같이 쌍따옴표, 홑따옴표가 출력되도록 코드를 작성해보시오.
# 나는 엄마에게 말했다. "더 이상 '카레'는 먹기 싫어요!"라고..

# [1]
a = """나는 엄마에게 말했다. "더 이상 '카레'는 먹기 싫어요!"라고..."""
b = "나는 엄마에게 말했다. \"더 이상 '카레'는 먹기 싫어요!\"라고..."

# [2] : 출력
print('[결과출력]')
print(a)
print(b)


print()


# 아래 코드의 결과로 출력되는 값들에 대해서 설명하시오.
# id() 함수는 무엇을 출력하는가?
# 3개의 id 출력 값중 다른 값을 출력하는 것이 있다면 몇번이고 왜 그런지 그 이유를 설명하시오.

# [1]
a = '붕어빵'
print(a, '-->', id(a))

# [2]
b = a
print(b, '-->', id(b))

# [3]
a = '잉어빵'
print(a, '-->', id(a))


print()


# 파이썬 문법중 is 연산자를 이용한 출력 결과를 설명하시오.
# 아래 코드의 결과로 출력되는 값은 무엇인지 말해보시오. ( True, False 둘중 하나로 출력됨 )

# [1]
a = [ 1, 2, 3, 4, 5 ]
b = a
c = [ 1, 2, 3, 4, 5 ]

# [2]
print( '[2-1] a is b = ', a is b )
print( '[2-2] a is c = ', a is c )
print( '[2-3] b is c = ', b is c )

# [Summary]
# is 연산자는 ==연산자와 달리 들어있는 데이터 값을 비교하는게 아니라 같은 객체를 가르치는지 비교함
# 그러므로, 설령 같은 값을 있다 하더라도 각각 다르게 생성된 객체라면 is 연산자로 비교시 False 값을 출력받게 된다.
# 위 코드에서 c에 할당된 리스트 객체는 새롭게 메모리 공간을 할당받아 새롭게 생성된 객체이기 때문에 첫번째 리스트 객체와는 다르게 된다.


print()


# 파이썬 문법중 == 연산자를 이용한 출력 결과를 설명하시오.
# 아래 코드의 결과로 출력되는 값은 무엇인지 말해보시오. ( True, False 둘중 하나로 출력됨 )

# [1]
a = [1, 2, 3, 4, 5]
b = a
c = [1, 2, 3, 4, 5]

# [2]
print('[2-1] a==b =', a==b)
print('[2-2] a==c =', a==c)
print('[2-3] b==c =', b==c)

# [Summary]
# == 연산자는 오브젝트의 데이터 값이 같은지를 확인하고자 할 때 사용한다.


print()


# 아래 코드의 is, == 연산자의 결과로 출력되는 값을 예상하여 말해보시오.
# 결과는 True, False 값으로 출력된다.

# [1] : 숫자
a = 101
b = 100 + 1
print(id(a), id(b))                 
print( '[1-1] a is b = ', a is b )  
print( '[1-2] a == b = ', a == b )

# [2] : 문자열
c = 'korea'
d = 'korea'
print(id(c), id(d))                 
print( '[2-1] c is d = ', c is d )  
print( '[2-2] c == d = ', c == d )

# [3] : 리스트
e = [1, 2, 3, 4, 5]
f = [1, 2, 3, 4, 5]
print(id(e), id(f))                 # 리스트는 값이 같아도 같은곳을 지정하지 않아서 id가 다름
print( '[3-1] e is f = ', e is f )  # 둘이 다르기 때문에 False
print( '[3-2] e == f = ', e == f )


print()


# 아래 코드의 is 연산자 결과 및 각각의 print 결과를 예상하여 말해보시오
a = "korea"
print( '[1]', a, id(a) )
b = "korea"
print( '[2]', b, id(b) )
print( 'a is b = ', a is b )
b += "!"                        # b : korea!
print( '[3]', b, id(b) )
print( 'a is b = ', a is b )
c = b[:-1]                      # b : korea
print( '[4]', c, id(c) )
print( 'a is c = ', a is c )    # 슬라이스 한 순간 새로운 값을 할당하기 때문에 False


print()


# 문자열을 slice한 결과와 id() 및 is() 연산자 출력 결과를 말해보시오.

# [1] : 문자열
t = "korea"

# [2] : 슬라이스 및 id() 출력
print(t, id(t), ' - ', t[:1], id(t[:1]), ' - ', t[:2], id(t[:2]), ' - ', t[:3], 
id(t[:3]), ' - ', t[:4], id(t[:4]) )
print( t, id(t[:]) )

# [3] : is 연산자 결과
print( 't is t[:] = ', t is t[:] )              # 어떤 변화도 주지 않았기 때문에 같은 값
print( 't is t[:1] = ', t is t[:1] )
print( 't[:1] is t[:2] = ', t[:1] is t[:2] )
print( 't[:] is t[:5] = ', t[:] is t[:5] )


print()


# a, b 각각의 변수에 들어있는 값을 교환하는 코드를 작성하시오.
# a, b 변수에 들어있는 값은 100, 200 이다.

# [1] : 변수 선언 및 값 할당
a = 100
b = 200
print('[1] a, b 변수의 값은 = ', a, b)

# [2] : temp 변수를 이용한 swap
temp = a                # a의 값을 temp에 빼놓는다.
a = b
b = temp
print('[2] a, b 변수의 값은 = ', a, b)


print()


# a, b 각각의 변수에 들어있는 값을 교환하는 코드를 작성하시오.
# a, b 변수에 들어있는 값은 100, 200 이다.
# 이때 별도의 temp 변수를 만들어서 교환하지 않고 한줄로 코드를 작성하여 교환하시오.
# 아래의 코드를 수정하시오.

# [1] : 변수 선언 및 값 할당
a = 100
b = 200
print( '[1] a, b 변수의 값은 = ', a, b )

# [2] : temp 변수를 이용하지 않고 swap
a, b = b, a
print( '[2] 교환 후 a, b 변수의 값은 = ', a, b )