# ;을 사용해 문장 구분
x = 5; y = 2

# \을 사용해 행 연결
z = x + \
y

print(z)


# built-in function

# 1. help()
help("if")
help(print)

# 2. dir(), 사용 가능한 네임스페이스의 이름을 출력
print(dir()) # 전역 네임스페이스 확인
print(dir(str)) # 내장 클래스인 str 클래스에서 정의하는 이름을 나열한다.

import math
print(dir(math))
 