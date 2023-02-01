# Chapeter03-2
# 파이썬 문자형

# 문자열 생성
str1 = "I am Python"
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4))

print()

# 빈 문자열
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))

print()

# 이스케이프 문자 사용
"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
...

"""
# I'm Boy

print("I'm Boy")
print('I\'m Boy')           # print('I'm Boy') 하면 오류가 나기 때문에 \를 앞에 써야 함
print('I\\m Boy') 

print('a \t b')             # 키보드의 탭 키만큼 간격이 벌어짐
print('a \n b')             # 줄바꿈
print('a \"\" b')           # 큰따옴표 두개를 이스케이프 하여 표현

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)
escape_str2 = 'What\'s on TV?'
print(escape_str2)

print()

# 탭, 줄 바꿈
t_s1 = "Click \t Start!"
t_s2 = "New Line \n Check!"

print(t_s1)
print(t_s2)

print()

# Raw String (앞에 소문자 r 붙이기, 있는 그대로 표시, 드라이브 경로 지정할때 주로 표시)
raw_s1 = r'D:\python\test'
print(raw_s1)

print()

# 멀티라인 입력(여러줄에 걸쳐서 한번에 입력, 역슬래시를 앞에 선언해두면 여러줄로 쓸 수 있음)
multi_str = \
"""
아리랑
사랑아 내 사람아 
불러도 대답없는 내 사람아 
같은하늘아래 살아도 다시는 못볼사람~ 
나는 천번을 다시 태어나도 그댈사랑합니다~ 
오늘도 기다리는 나를 잊지는 말아요~
"""

print(multi_str)

print()

# 문자열 연산
str_o1 = "python"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul Daejeon Daegu Busan"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)                # str_o1 안에 'y'가 있는지 묻는것!(있으면 True, 없으면 False)
print('z' in str_o1)
print('P' not in str_o2)            # 대문자 P가 없는지!

print()

# 문자열 형 변환
print(str(66), type(str(66)))       # 문자 66을 의미
print(str(10.1))
print(str(True), type(str(True)))

print()

# 문자열 함수(upper, isalnum, startswith, count, endswith, isalpha...)

print("Capitalize : ", str_o1.capitalize())          # 첫번째 시작 글자를 대문자로 바꿔줌
print("endswith : ", str_o2.endswith("e"))           # 마지막 문자가 뭘로 끝나는지 확인
print("replace : ", str_o1.replace("thon", "Good"))  # 앞부분을 찾아서 뒷부분으로 바꿀때 사용
print("sorted : ", sorted(str_o1))
print("split : ", str_o4.split(' '))                 # 특정 단위로 분리할때

print()

#  반복(시퀀스) 
im_str = "Good Boy!"

print(dir(im_str))          # __iter__ 가 있으면 반복할수있음

# 출력
for i in im_str:
    print(i)

print()

# 슬라이싱
str_s1 = "Nice Python"

print(len(str_s1))          # 0부터 10이니까 11한글자!!

print()

# 슬라이싱 연습
print(str_s1[0:3])              # 0 1 2 나와라(3-1)
print(str_s1[5:11])             # 5 6 7 8 9 10
print(str_s1[5:])               # 5부터 끝까지
print(str_s1[:len(str_s1)])     # str_s1[:11]
print(str_s1[:len(str_s1)-1])   # str_s1[:10]
print(str_s1[1:9:2])            # 1부터 9까지 가져오는데 2칸 간격으로 가져와라
print(str_s1[-5:])              # 뒤에서 부터 -1, -5부터 끝까지 나와라
print(str_s1[1:-2])
print(str_s1[::2])              # 처음부터 끝까지 두칸 간격으로 가져와라
print(str_s1[::-1])             # 처음부터 끝까지 가져오는데 순서를 반대로 가져와라
print(str_s1[::-2])

print()

# 아스키 코드(유니코드)
a = 'z'
print(ord(a))           # 아스키 코드로
print(chr(122))         # 문자로