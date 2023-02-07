# 파이썬 사용자 입력
# Input 사용법
# 기본타입(str)

# 예제 1
# name = input("Enter Your Name")
# grade = input("Enter Your Grade")
# company = input("Enter Your Company Name")

# print(name, grade, company)


# 예제 2
# number = input("Enter Number : ")
# name = input("Enter Name : ")

# print("type of number", type(number))
# print("type of name", type(name))


# 예제 3
# first_number = int(input("Enter Number1 : "))           # 문자열로 인식을 하기때문에 형변환 하여 사용
# second_number = int(input("Enter Number2 : "))

# total = first_number + second_number
# print("first_number + second_number : ", total)


# 예제 4
float_number = float(input("Enter float number : "))

print("input float : ", float_number)
print("input type : ", type(float_number))

# 예제 5
print("FirstName - {0}, LastName - {1}".format(input("Enter first name : "), input("Enter second name : ")))