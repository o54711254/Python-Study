import sys

print(sys.path)

print(type(sys.path))

# 모듈 경로 삽입
sys.path.append('C:/python_basic')

# print(sys.path)

import 모듈

# 모듈 사용
# print(test_module.power(10, 3))

import 모듈
print(모듈.add(10, 110))