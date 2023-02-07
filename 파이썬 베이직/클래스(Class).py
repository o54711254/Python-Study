# 파이썬 클래스
# OOP(객체 지향 프로그래밍), Self, 인스턴스 메소드, 인스턴스 변수

# 클래스 and 인스턴스 차이 이해
# 네임스페이스 : 객체를 인스튼서화 할 때 저장된 공간
# 클래스 변수 : 직접 접근 가능, 공유
# 인스턴스 변수 : 객체마다 별도 존재

# 예제 1
class Dog: # object를 상속받기에 써도되고 생략해도됨
    # 클래스 속성
    species = 'firstdog'            # 클래스 변수

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 클래스 정보
print(Dog)

# 인스턴스화
a = Dog("오달수", 2)
b = Dog("박범식", 3)
c = Dog("조봄", 2)

# 비교
print(a == b)

# 네임스페이스
print('dog1', a.__dict__)
print('dog2', b.__dict__)
print('dog3', c.__dict__)


# 인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.age))

print(Dog.species)
print(a.species)
print(b.species)

# 예제 2
# self의 이해
class Selftest:
    def func1():
        print('Func1 called')
    def func2(self):
        print('Func2 called')


f = Selftest()

# print(dir(f))
print(id(f))
f.func2()

Selftest.func1()

print()


# 예제 3
# 클래스 변수, 인스턴스 변수
class Warehouse:
    stock_num = 0           # 클래스 변수 = 0

    def __init__(self, name):
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):
        Warehouse.stock_num -= 1


user1 = Warehouse('Lee')
user2 = Warehouse('Cho')

print(Warehouse.stock_num)


print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print(Warehouse.__dict__)

del user1

print(Warehouse.stock_num)

print()


# 예제 4
class Dog: # object를 상속받기에 써도되고 생략해도됨
    # 클래스 속성
    species = 'firstdog'            # 클래스 변수

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return '{} is {} years old'.format(self.name, self.age)
    
    def speak(self, sound):
        return "{} says {}!".format(self.name, sound)
    

# 인스턴스 생성
c = Dog('July', 4)
print(c.info())
print(c.speak('Wal Wal'))