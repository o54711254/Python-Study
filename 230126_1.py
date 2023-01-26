# Chapter02-1
# 파이썬 완전 기초
# Print 사용법

# 기본 출력
print('Python Start!')
print("2023-01-26")
print('''오건영''')
print("""화이팅!""")

print()

# seperator 옵션
print('P', 'Y', 'T', 'H', 'O', 'N', sep='')
print('010', '5471', '1254', sep='-')
print('o54711254', 'gmail.com', sep='@')

print()

# end 옵션

print('Welcome to', end=' ')
print('IT News', end=' ')
print('Web Site')

# file 옵션
import sys
print('Learn Python', file=sys.stdout)
print()

# format 사용(d : 정수, s : 문자열, f : 실수)

print('%s %s' % ('one', 'two')) #메모되나?
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two')) #{}안은 암묵적으로 01234순서로 가기 때문

# %s

print('%10s' % ('nice'))       # 양수는 왼쪽부터 공백으로 채움
print('{:>10}'.format('nice')) # 위랑 같은거인데 왼쪽이라고 표시한거

print('%-10s' % ('nice'))      # 음수는 오른쪽부터 공백으로 채움
print('{:10}'.format('nice'))  # 생략하면 오른쪽을 공백으로 채움
     
print('{:_>10}'.format('nice')) # 원하는기호로 채울 수 있음
print('{:_^10}'.format('nice')) # 중앙정렬은 '^' 표시

print('%.5s' % ('Pythonstudy')) # .을 찍으면 다섯개 절삭, 숫자면 반올림
print('{:10.5}'.format('Pythonstudy')) # 총 10개의 자리를 확보하는데 다섯개만 나와라
print('%-10.5s' % ('Pythonstudy'))


# %d

print('%d %d' % (1, 2))
print('{} {}'.format(1, 2))

print('%4d' % (54))
print('{:4d}'.format(54))


# %f 

print('%1.4f' % (3.1415922222)) # 총 자릿수는 한자리, 소수점은 4자리(반올림)
print('{:1.4f}'.format(3.1415922222))

print('%06.2f' % (3.141592653589793)) # 총 자릿수는 6개, 소수 2자리까지이기 때문에 정수부를 0으로 채움
print('{:06.2f}'.format(3.141592653589793))



# 복습
print('%s %s' % ('오건영','존멋'))
print('{} {}'.format('오건영', '존멋'))
print('%d %d' % (1, 2))
print('{} {}'.format(1, 2))

print('%f' % (0.01054711254))
print('%0.11f' % (0.01054711254))