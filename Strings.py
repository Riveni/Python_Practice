# Creating a string can be done by using "" or ''
str1 = "this is string"
str2 = 'this is also'

# Strings arithmetic
str3 = str1 + str2  # joining strings
str4 = str1 * 2  # multiple strings

# Special chars
# \n :new line
# \t : tab
""" 
  triple quotes allows typing without using special chars and also for long comments
"""

# Accessing char in string
char1 = str1[0]
char2 = str1[-1]  # (-1) is the last char in the string
# Strings slicing
str1[0:4]  # return chars 0-3
# Slicing with step: string[START:STOP:STEP]

# String type is immutable, meaning it is not possible to change single char
# in existing string: str1[0] = 'a' -> ERROR
# Therefore, in order to change a char in string we have to change the whole string
