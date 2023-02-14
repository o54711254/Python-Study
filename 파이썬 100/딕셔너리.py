# 파이썬의 딕셔너리 자료형은 무엇인지 설명하시오.
# 딕셔너리 타입의 특징에 대해서 말해보시오.
# 딕셔너리 타입 관련하여 다양한 예제를 통해서 설명해보시오. 삽입, 수정, 삭제도 구현해보시오.

# [!] : 딕셔너리(dict)
# 키(key)와 값(value)이 하나의 쌍으로 이루어진 데이터 값
# {key:value}
# 순서없이 저장 --> 입력한 데이터 값에 접근할 때는 key를 참조하여 접근 --> index 접근이 불가능 --> dic[0]이런거 에러
# key 값은 중복도 안되고, 변경도 불가능. 중복된 key값이 입력은 가능하나 기존 값이 대체되어 버림
# value 값은 중복, 변경 가능
# 데이터 입력을 숫자, 문자 외에도 리스트와 배열 객체로도 입력 가능

# [1] : 딕셔너리 선언
dict_ = {}

# [2] : 데이터 입력
dict_['id'] = 'hong'
dict_['name'] = '홍길동'
dict_['age'] = '20'
dict_['hp'] = '010-1234-5678'
dict_['address'] = '서울'

print(dict_)

print('-'*100)

# [3] : 데이터 출력
print(dict_['id'])
print(dict_['name'])
print(dict_['age'])
print(dict_['hp'])
print(dict_['address'])

print(dict_['id'], dict_['name'], dict_['age'], dict_['hp'], dict_['address'])

print('-'*100)

# [4] : 반복문을 사용한 데이터 출력 -key
for i in dict_.keys():
    print(i, end=' ')

print()

print('-'*100)

# [5] : 반복문을 사용한 데이터 출력 -value
for i in dict_.values():
    print(i, end=' ')

print()

print('-'*100)

# [6] : key, value 모두 출력
for i in dict_.items():
    print(i)
print()

print('-'*100)

# [7] : 빈 딕셔너리만들기
a = dict()
b = {}
print(a, type(a))
print(b, type(b))

print('-'*100)

# [8] : 가독성
dict1 = {
            'name':'홍길동',
            'id':'hongkildong',
            'age':20
}
print(dict1)
print(dict1['name'])

print('-'*100)

# [9] : 중첩 딕셔너리(Nested Dictionary)
dict2 = {
            'name':'을지문덕',
            'age':30,
            'pastime':{
                'reading':30,
                'walking':60
            }
}
print(dict2)
print(dict2['pastime'])
print(dict2['pastime']['walking'])

print('-'*100)

# [10] : 삽입, 수정, 삭제
dict3 = {
            'name':'홍길도',
            'id':'hong'
}
print(dict3)

dict3['age'] = 22       # 삽입
print(dict3)

dict3['age'] = 33       # 수정
print(dict3)

del dict3['age']        # 삭제
print(dict3)
