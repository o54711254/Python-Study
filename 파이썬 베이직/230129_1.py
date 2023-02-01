# Chapter 03-3
# 파이썬 리스트
# 자료구조에서 중요
# 리스트 자료형(순서o, 중복o, 삭제o)


# 선언
a = []
b = list()
c = [70, 75, 80, 85] #Len
d = [1000, 10000, 'Ace', 'Base', 'Captine']             # 서로 다른 자료형을 한 리스트안에 담을 수 있음
e = [1000, 10000, ['Ace', 'Base', 'Captine']]           # 리스트안에 리스트를 담을 수 있음
f = [21.42, 'foobar', 3, 4, False, 3.141592]


# 인덱싱            # 내가 원하는 데이터를 꺼내오는 과정
print('>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1][1])
print('e - ', list(e[-1][1]))

# 슬라이싱
print('>>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[-1][1:3])

# 리스트 연산
print('>>>>>>')
print('c + d', c + d)
print('c * 3', c * 3)
print("'Test' + c[0]", 'Test' + str(c[0]))          # c[0]을 문자형으로 형 변환 후 연산

# 값 비교
print('>>>>>>')
print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])

# identity(id)
print('>>>>>>')
temp = c
print(temp, c)
print(id(temp))
print(id(c))

# 리스트 수정, 삭제
print('>>>>>>')
c[0] = 4
print('c - ', c)
c[1:2] = ['a', 'b', 'c']
print('c - ', c)            # 리스트와의 연산은 리스트로 하기 때문에 리스트 안의 원소 'a', 'b', 'c' 가 들어감
c[1:2] = ['a', 'b', 'c']
print('c - ', c)
print(len(c))
print(c)
c[1:3] = []
print(c)
del c[2]            # 삭제
print('c - ', c)

# 리스트 함수
print('>>>>>>')
a = [5, 2, 3, 1, 4]
print('a - ', a)
a.append(6)             # 끝부분에 데이터 삽입할때 사용
print(a)
a.sort()                # 숫자 정렬
print(a)
a.reverse()             # 역순으로 숫자 정렬
print(a)
print(a.index(3), a[3]) # 같은 방법
a.insert(2, 7)          # 자리 2에 숫자 7을 넣는다
print(a)
# del a[]
a.remove(6)
print(a)             # del은 자리에 있는 값을 지우고 remove는 값을 찾아서 지움
print(a.pop())                 # 기존 원소들 중 제일 마지막 값을 지움
print(a)
print(a.count(4))       # 내가 원하는값이 안에 몇개 있는지 확인
ex = [8, 9]
a.extend(ex)            # 확장
print(a)

# 삭제 : remove, pop, del

# 반복문 활용
while a:
    data = a.pop()
    print(data)