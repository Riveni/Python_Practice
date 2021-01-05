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