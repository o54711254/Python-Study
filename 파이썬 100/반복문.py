# 0부터 9까지 출력하는 for 반복문 예제를 구현하시오.

# [1] : for반복문
for i in range(10):     # 0 ~ 9 10개를 반복한다., i 대신 아무거나 써도 됨
    print(i)

print('-'*50)

# 아래의 for 반복문 예제중에서 틀린곳을 찾아서 말해보시오.

# [1]
for i in range(10):
    print(i)

# [2]
for i in range(10): print(i)

# [3]
# for i in range(10):
# print(i) --> 들여쓰기를 안해서 에러가 남

print('-'*50)


# 0부터 9까지 숫자가 아래처럼 출력되도록 for 반복문 예제를 구현하시오.
# 0 1 2 3 4 5 6 7 8 9

for i in range(10):
    print(i, end = ' ')         # end 옵션

print()

print('-'*50)

# 0부터 9까지 숫자가 아래처럼 출력되도록 for 반복문 예제를 구현하시오.
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9      9끝에 , 없음

# [1]
n = 0
for i in range(10):
    if n < 9:
        print(i, end=', ')
    else :
        print(i)
    n = n+1

print()

# [2] 
for i in range(10):
    if i < 9:
        print(i, end = ', ') 
    else:
        print(i)

print()

print('-'*50)

# for 반복문을 사용하여 4부터 21까지의 홀수들의 합을 구하는 코드를 구하시오
sum_odd = 0
for i in range(4, 22):
    if i % 2 == 1:            # 2로 나누었을때 나머지가 1이 나오면 홀수이므로, 2!=0해도 됨
        sum_odd += i
print()

print(sum_odd)

print('-'*50)

# 1부터 100까지의 수에서 짝수들만 출력하는 코드를 구현하시오.
# 두가지 방식을 생각해서 구현해보시오

# [1]
for i in range(1,101):
    if i % 2 == 0:
        print(i, end=' ')
print()

# [2] : range 함수의 step(간격) 옵션을 이용하여 처리.
for i in range(2, 101, 2):
    print(i, end=' ')
print()

print('-'*50)

# for 반복문을 사용하여 구구단 전체를 출력하는 코드를 구현하시오.

# [1] 구구단
for i in range(2, 10):
    print(i, '단')
    for j in range(1, 10):
        print(i, 'X', j, '=', i*j)
    print()         # 간격용

print()


print('-'*50)


# 리스트 요소의 값을 반복문을 사용하여 모두 출력하시오.
# 이때 가로로 값을 출력하시오.
# 값을 모두 출력한 후에는 끝에 요소의 갯수를 함께 출력시키시오.

# [1] : 리스트
lst = ['dog', 'hippo', 'elephant', 'lion', 'tiger', 'aligator']

# [2] : 반복문
for i in range(len(lst)):
    print(lst[i], end=' ')

print(len(lst))

print()

# 리스트 요소의 값을 반복문을 사용하여 거꾸로 출력시키시오.

# [1] : 리스트
lst = [1, 2, 3, 4, 5]

# [2] : 반복문 --> 거꾸로 출력
for i in lst[::-1]:         # ::1하면 순서대로, ::-1 하면 거꾸로 출력
    print(i, end=' ')

print()