# Identity Comparison with 'is' and 'id()'
a = 1.0
b = 1.0
print(a is b)    # True
print(a is not b)  # False

# Built-in Functions
print(pow(2, 3))          # 8, equivalent to 2 ** 3

print(abs(-10))           # 10
print(abs(3 + 4j))        # 5.0, magnitude of the complex number

print(round(3.141592, 3))  # 3.142

print(bin(10))            # 0b1010

print(int('0b1010', base=2))  # 10
print(int(oct(10), base=8))   # 10

print(ord('A'))           # 65
print(chr(65))            # A