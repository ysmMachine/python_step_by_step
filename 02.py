# sequence: 순서가 있는 자료형 ex) str, bytes, list, tuple, range
# collection: sequence + (dict, set)


# type
print(type(b"abc")) # <class 'bytes'>
print(type("abc")) # <class 'str'>
print(type(1))# <class 'int'>
print(type(range(0, 10))) # <class 'range'>


# 변수명은 숫자로 시작할 수 없고, 키워드를 사용할 수 없다.
import keyword
print(keyword.kwlist)
print(keyword.iskeyword("if")) # True


# 복소수형 자료
x = 1 + 2j # x = complex(1, 2)
print(type(x)) # <class 'complex'>
print(x.real) # 1.0
print(x.imag) # 2.0
print(x.conjugate()) # (1 - 2j), 켤레 복소수


# escape sequence
print("AB\tCD")
print("C:\name") # \n: new line(Enter key)
print(r"C:\name") # r: raw 
print("\x41") # 16진수 41 = 65 = A


# isinstance()
print(isinstance(10, (int, float))) # int or float


# 콤마(,) 연산자와 지정문
x, y = 1, 2 # 내부적으로는 지정문 오른쪽을 실행하여 튜플 (1, 2)를 생성하고, 튜플을 언패킹하여 x = 1, y = 2를 저장
x, y = y, x # 내부적으로는 지정문 오른쪽을 실행하여 튜플 (2, 1)을 생성하고, 튜픙릉 언패킹하여 x = 2, y = 1을 저장

