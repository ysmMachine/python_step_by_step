# Sequences and Collections
# Sequences: Ordered data types (str, bytes, list, tuple, range)
# Collections: Sequences + (dict, set)

# Type Checking
print(type(b"abc"))          # <class 'bytes'>
print(type("abc"))           # <class 'str'>
print(type(1))               # <class 'int'>
print(type(range(0, 10)))    # <class 'range'>

# Variable Naming Rules
# Variables cannot start with a number or use keywords.
import keyword
print(keyword.kwlist)        # List of all keywords
print(keyword.iskeyword("if")) # True

# Complex Numbers
x = 1 + 2j  # x = complex(1, 2)
print(type(x))             # <class 'complex'>
print(x.real)              # 1.0
print(x.imag)              # 2.0
print(x.conjugate())       # (1 - 2j)

# Escape Sequences
print("AB\tCD")            # AB    CD
print("C:\name")           # C:
                           # ame
print(r"C:\name")          # C:\name (raw string, no escape)
print("\x41")              # A (hexadecimal 41 = 65 = A)

# isinstance() Function
print(isinstance(10, (int, float)))  # True (10 is either int or float)

# Comma Operator and Assignment
x, y = 1, 2  # Tuple (1, 2) is created and unpacked: x = 1, y = 2
x, y = y, x  # Tuple (2, 1) is created and unpacked: x = 2, y = 1