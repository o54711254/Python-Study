# Chater 04-02
# 파이썬 반복문
# for 실습

# 코딩의 핵심
# for in <collection>
#   <Loop body>

for v1 in range(10):            # 0 ~ 9까지 10개의 원소 출력
    print('v1 is :', v1)

print()

for v2 in range(1, 11):         # 1~10
    print('v2 is :', v2)

print()

for v3 in range(1, 11, 2):      # 1~10까지 두개씩 스킵하면서
    print('v3 is :', v3)

print()


# 1 ~ 1000까지의 합

sum1 = 0

for v in range(1, 1001):
    sum1 += v

print('1~1000 sum :', sum1)

print('1~1000 Sum :', sum(range(1,1001)))

print(type(range(1, 11)))

print('1 ~ 1000 4의 배수의 합 :', sum(range(4, 1001, 4)))


print()


# Iterables 자료형 반복(Iterable은 반복가능하다는거)
# 문자열, 리스트, 튜플, 집합, 사전(딕셔너리)
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

# 예제1
names = ['Kim', 'Park', 'Cho', 'Lee', 'Choi', 'Yoo']

for n in names:
    print('You are :', n)

# 예제2
lotto_number = [11, 19, 21, 28, 36, 37]

for n in lotto_number:
    print('current number :', n)

# 예제3
word = "Beautiful"

for s in word:
    print('word :', s)

# 예제4
my_info = {
    "name": 'Oh',
    "Age": 28,
    "City": 'Daejeon'
}

for k in my_info:
    print('key :', my_info[k])          # 값을 나오게 하기 위해 my_info[k] 사용

for v in my_info.values():
    print('value :', v)


# 예제5
name = 'FineAppLE'

for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())


# break(반복의 흐름을 제어)

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 34:
        print('Found 34!')
        break
    else:
        print('Not found :', num)


print()


# continue

lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is bool:
        continue
    print("current type :", v, type(v))
    print("multiply by 2", v * 2)

print()


# for - else(파이썬의 독보적인 기능)

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 49:
        print('Found : 49')
        break
else:                           # for, else가 같은 자리에 있음
    print('Not Found : 49')     # 끝까지 찾았지만 없었다. 이런느낌


print()

# 구구단 출력

for i in range(2, 10):
    for j in range(1, 10):
        print('{:4d}'.format(i*j), end='')          # end='' : 줄바꿈 안되게, '{:4d}' : 네자리 정수형
    print()


# 변환 예제
name2 = 'Aceman'

print('Reversed', reversed(name2))
print('List', list(reversed(name2)))
print('tuple', tuple(reversed(name2)))
print('set', set(reversed(name2)))          # 순서 x, 실행할때마다 위치 랜덤
