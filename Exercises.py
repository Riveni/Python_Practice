# Ex.1
"""
total_bricks = input("enter number of bricks for each pig:")
total_bricks = int(total_bricks)
a = total_bricks // 100
total_bricks = total_bricks % 100
b = total_bricks // 10
c = total_bricks % 10
bricks_sum = a + b + c
divide = bricks_sum // 3
redundancy = bricks_sum % 3
print(bricks_sum, divide, redundancy, redundancy == 0, sep="\n")
"""

# Ex.2
"""
print("\"Shuffle, Shuffle, Shuffle\", say it together!\n"
      "Change colors and directions, \n"
      "Don't back down and stop the player!\n"
      "\tDo you want to play Taki?\n"
      "\tPress y\\n")
"""

# Ex.3
"""
encrypted_message = "!XgXnXiXcXiXlXsX XnXoXhXtXyXpX XgXnXiXnXrXaXeXlX XmXaX XI"
decrypt = encrypted_message[::-2]
print(decrypt)
"""

# Ex.4
"""
sen = input("Enter your string: ")
print(sen[0] + sen[1:].replace(sen[0], 'e'))
"""

# Ex.5
"""
word = input("Enter a word: ").lower().replace(" ", "")
rev = word[::-1]
if word == rev:
    print("OK")
else:
    print("NOT")
"""

# Ex.6
"""
import calendar
date = input("Enter a date: ")
day, month, year = date.split("/")
week_day = calendar.weekday(int(year), int(month), int(day))
if week_day == 0:
    print("Monday")
elif week_day == 1:
    print("Tuesday")
elif week_day == 2:
    print("Wednesday")
elif week_day == 3:
    print("Thursday")
elif week_day == 4:
    print("Friday")
elif week_day == 5:
    print("Saturday")
elif week_day == 6:
    print("Sunday")
"""

# Ex.7
"""
def last_early(my_str):
    if my_str[-1] in my_str[:-1]:
        print("True")
    else:
        print("False")


last_early("best of luck")
"""

# Ex.8
"""
def distance(num1, num2, num3):
    if (abs(num1 - num2) == 1 or abs(num1 - num3) == 1) and (abs(num1 - num2) > 1 or abs(num1 - num3) > 1):
        print("True")
    else:
        print("False")


distance(1, 2, 10)
"""

# Ex.9
"""
def fix_age(age):
    age = 0
    return age


def filter_t(a=13, b=13, c=13):
    if 12 < a < 15 or 16 < a < 20:
        a = fix_age(a)
    if 12 < b < 15 or 16 < b < 20:
        b = fix_age(b)
    if 12 < c < 15 or 16 < c < 20:
        c = fix_age(c)
    print(a + b + c)

filter_t()
filter_t(1, 2, 3)
filter_t(2, 13, 1)
filter_t(2, 1, 15)
"""

# Ex.10
"""
SMALL_LENGTH = 1
BIG_LENGTH = 5


def chocolate_maker(small, big, x):
    if (small * SMALL_LENGTH + big * BIG_LENGTH >= x) and (x % BIG_LENGTH <= small):
        print("True")
    else:
        print("False")


chocolate_maker(0, 3, 13)
chocolate_maker(3, 1, 8)
chocolate_maker(3, 1, 9)
chocolate_maker(3, 2, 10)
"""

# Ex.11 - defining main function
"""
def my_func(num1, num2):
    return num1 * num2


def main():
    multi = my_func(2, 5)
    print(multi)


if __name__ == "__main__":
    main()
"""

# Ex.12 - working with lists
'''
def shift_left(my_list):
    """Cyclic shift lists' elements to the left"""
    var = my_list.pop(0)
    my_list.append(var)
    print(my_list)


shift_left([1, 2, 3])
shift_left(['monkey', 2.0, 1])
'''

# Ex.13
"""
def format_list(my_list):
    sep = ', '
    print(sep.join(my_list[::2]) + ", and " + my_list[-1])


format_list(["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"])
"""

# Ex.14
"""

def extend_list_x(list_x, list_y):
    # list_x[:0] = list_y
    list_x = list_y + list_x
    # list_x.extend(list_y)
    print(list_x)


def main():
    y = [1, 2, 3]
    x = [4, 5, 6]
    extend_list_x(x, y)
    print(x)


if __name__ == "__main__":
    main()
"""
