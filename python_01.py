# Using Semicolon (;) to Separate Statements
x = 5; y = 2

# Using Backslash (\) to Continue a Statement Across Multiple Lines
z = x + \
    y

print(z)  # 7

# Built-in Functions

# 1. help() Function
help("if")    # Displays information about the 'if' statement
help(print)   # Displays information about the 'print' function

# 2. dir() Function - Lists the Names in a Namespace
print(dir())        # Lists the names in the global namespace
print(dir(str))     # Lists the attributes and methods of the 'str' class

# Using 'dir()' with a Module
import math
print(dir(math))    # Lists the attributes and methods of the 'math' module