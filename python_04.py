# String Indexing
s = 'abcd'  # s[0] == s[-4]

# Sequence Slicing
# s[start:stop:step]
# start <= i < stop, i += step
s = "abcdefg"
print(s[:2])        # ab
print(s[:])         # abcdefg
print(s[::2])       # aceg
print(s[::-1])      # gfedcba
print(s[-3:])       # efg
print(s[slice(2)])  # ab

# Sequence Length
print(len(range(1, 6)))       # 5
print(len(b"abc"))           # 3
print(len((1, 2, 3, 4, 5)))  # 5
print(len(set([1, 2, 3, 4]))) # 4

# String Operations
print("ab" + "bc")               # abbc
print('ell' in 'hello')          # True
print('abcd' < 'abce')           # True
x, y, z = "abc"
print(x, y, z)  # a b c

# String Methods
s1 = "ab12"
print(s1.isalpha())  # False
print(s1.isalnum())  # True

s2 = "aBc"
print(s2.islower())  # False
print(s2.isupper())  # False

s3 = "123"
print(s3.isdigit())  # True
print(s3.isnumeric())  # True

# Strip Whitespace
s = ' apple '
print(s.lstrip())  # 'apple '
print(s.rstrip())  # ' apple'
print(s.strip())   # 'apple'

# Join Strings
alpha = 'a b c'
li = alpha.split(' ')
print(li)  # ['a', 'b', 'c']
join_alpha = "".join(li)
print(join_alpha)  # abc

# String Formatting
x, y, z = 10, 20, 30
print('{}, {}, {}'.format(x, y, z))  # 10, 20, 30