# Chapter 03-5
# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용
# 딕셔너리 자료형(순서x, 키 중복x, 수정o, 삭제o)

# 선언
a = {'name': 'Oh', 'Phone': '01054711254', 'birth': '961211'}
b = {0: 'Hello Python'}
c = {'arr': [1, 2, 3, 4]}
d = {
    'Name': 'Oh kun young',
    'City': 'Daejeon',
    'Age': 28,
    'Grade': 'A+',
    'Status': True
}
e = dict([
    ('Name', 'Oh kun young')            # 이런식으로 선언해도 됨
])

f = dict(                               # 많이 사용
    Name= 'Oh kun young',
    City= 'Daejeon',
    Age=28,
    Grade='A+',
    Status=True
)

print('a -', type(a), a)
print('b -', type(b), b)
print('c -', type(c), c)
print('d -', type(d), d)
print('e -', type(e), e)
print('f -', type(f), f)

print()

# 출력
print('a - ', a['name'])                # 키가 존재하지 않으면 에러
print('a - ', a.get('name'))            # 키가 없을경우 None이 나옴
print('b - ', b[0])
print('b - ', b.get('0'))
print('f - ', f.get('City'))
print('f - ', f.get('Age'))

# 딕셔너리 추가
a['address'] = 'Daejeon'
print('a - ', a)
a['rank'] = [1, 2, 3]
print('a - ', a)

# 딕셔너리 길이
print('a - ', len(a))
print('b - ', len(b))
print('c - ', len(c))
print('d - ', len(d))

print()

# dice_keys, dict_values, dict_item : 반복문(__iter__)에서 사용 가능

print('a -', a.keys())          # 키값들만 가져옴
print('b -', b.keys())          
print('c -', c.keys())          
print('d -', d.keys())         

print('a -', list(a.keys()))

print()

print('a -', a.values())          # 값들만 가져옴
print('b -', b.values())          
print('c -', c.values())          
print('d -', d.values())

print()

print('a - ', a.items())            # 키와 밸류가 한쌍으로 나옴
print('b - ', b.items())
print('c - ', c.items())
print('d - ', d.items())
print('a -', list(a.items()))

print()

print('a - ', a.pop('name'))
print('a - ', a)
print('c - ', c.pop('arr'))
print('c - ', c)

print()

print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)

print()

print('a - ', 'birth' in a)             # 딕셔너리에서 키를 포함하고 있는지를 조회
print('a - ', 'City' in d)

# 수정
a['test'] = 'test_dict'

print('a - ', a)

a['address'] = 'Seoul'
print('a - ', a)

a.update(birth='910904')
print('a - ', a)

temp = {'address': 'Busan'}
a.update(temp)
print('a - ', a)