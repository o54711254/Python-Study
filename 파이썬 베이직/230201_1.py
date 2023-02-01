# Chapter04-3
# 파이썬 반복문
# While 실습

# while <expr>:
#   <statemment(s)>


# 예 1

n = 5
while n > 0:
    print(n)
    n = n - 1


print()

# 예 2

a = ['foo', 'bar', 'baz']

while a:
    print(a.pop())

print()

# 예 3
# break, continue

n = 5
while n>0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Loop Ended.')

print()

# 예 4

m = 5
while m > 0:
    m -= 1
    if m == 2:
        continue
    print(m)
print('Loop Ended.')

print()


# if 중첩
# 예제 5
i = 1

while i <= 10:
    print('i:', i)
    if i == 6:
        break
    i += 1

print()


# While else 구문

# 예제 6
n = 10
while n > 0:
    n -= 1
    print(n)
    if n == 5:
        break
else:
    print('else out.')


print()

# 예제 7
a = ['foo', 'bar', 'baz', 'qux']
s = 'kim'

i = 0


while i < len(a):
    if a[i] == s:
        break
    i += 1
else:
    print(s, 'not found in list.')


# 무한반복
# while true:
#   print('foo')

# 예제 8
a = ['foo', 'bar', 'baz']

while True:
    if not a:
        break
    print(a.pop())