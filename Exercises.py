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

# Ex.15
"""
def are_lists_equal(list1, list2):
    if sorted(list2) in [sorted(list1)] and sorted(list1) in [sorted(list2)]:
        return True
    else:
        return False


def main():
    list1 = [0.6, 1, 2, 3]
    list2 = [3, 2, 0.6, 1]
    list3 = [9, 0, 5, 10.5]
    print(are_lists_equal(list1, list2))
    print(are_lists_equal(list1, list3))


if __name__ == "__main__":
    main()
"""

# Ex.16
"""
def longest(my_list):
    list1 = sorted(my_list, key = len )
    print(list1[-1])


def main():
    list1 = ["111", "234", "2000", "goru", "birthday", "09"]
    longest(list1)


if __name__ == "__main__":
    main()
"""

# Ex.17
"""
def squared_numbers(start, stop):
    num_list = []
    while start <= stop:
        num_list.append(start**2)
        start += 1
    return num_list


def main():
    print(squared_numbers(4, 8))
    print(squared_numbers(-3, 3))


if __name__ == "__main__":
    main()
"""

# Ex.18
"""
def is_greater(my_list, n):
    new_list = []
    for num in my_list:
        if num > n:
            new_list.append(num)
    return new_list


def main():
    result = is_greater([1, 30, 25, 60, 27, 28], 28)
    print(result)


if __name__ == "__main__":
    main()
"""

# Ex.19
"""
def seven_boom(end_number):
    l = []
    for num in range(end_number + 1):
        if (num % 7 == 0) or ('7' in str(num)):
            l.append("BOOM")
        else:
            l.append(num)
    return l


def main():
    print(seven_boom(17))


if __name__ == "__main__":
    main()
"""

# Ex.20
"""
def sequence_del(my_str):
    l = []
    perv_letter = ""
    for letter in my_str:
        if letter != perv_letter:
            l.append(letter)
        perv_letter = letter
    print("".join(l))


def main():
    sequence_del("ppyyyyythhhhhooonnnnn")
    sequence_del("SSSSsssshhhh")
    sequence_del("Heeyyy   yyouuuu!!!")


if __name__ == "__main__":
    main()
"""

# Ex.21
"""
def arrow(my_char, max_length):
    for i in range(max_length):
        print(my_char * (i +1))
    for i in range(i - 1, -1, -1):
        print(my_char * (i + 1))

def main():
    arrow('*', 5)


if __name__ == "__main__":
    main()
"""

# Ex.22
"""
data = ("self", "py", 1.543)
format_string = "Hello %s.%s learner, you have only %.1f units left before you master the course!"
print(format_string % data)
"""

# Ex.23
"""
def extract_key(product):
    return product[1]


def sort_prices(list_of_tuples):
    list_of_tuples.sort(key=extract_key)
    print(list_of_tuples)


def main():
    products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
    sort_prices(products)


if __name__ == "__main__":
    main()
"""

# Ex.24
"""
def count_chars(my_str):
    dict = {}
    for letter in my_str:
        if letter.isalpha():
            dict[letter] = my_str.count(letter)
    print(dict)


magic_str = "abra cadabra"
count_chars(magic_str)
"""

# Ex.25
"""
def inverse_dict(my_dict):
    new_dict = {}
    for key in my_dict:
        if my_dict[key] in new_dict:
            new_dict[my_dict[key]].append(key)
        else:
            new_dict[my_dict[key]] = [key]
    print(new_dict)


course_dict = {'I': 3, 'love': 3, 'self.py!': 2}
inverse_dict(course_dict)
"""

# Ex.26
"""
def are_files_equal(file1, file2):
    for line in file1:
        if line != file2.readline():
            return False
    if file2.readline() is not '':
        return False
    else:
        return True


def main():
    file1 = open(r"C:\file1.txt", "r")
    file2 = open(r"C:\file2.txt", "r")
    print(are_files_equal(file1, file2))
    file1.close()
    file2.close()


if __name__ == "__main__":
    main()
"""

# Ex.27
"""
def main():
    file_path = input(r"Enter file path:")
    action = input(r"Choose action(sort\rev\last):")
    file1 = open(file_path, "r")
    if action == "sort":
        word_list = []
        for line in file1:
            for word in line.split():
                if word not in word_list:
                    word_list.append(word)
        word_list.sort()
        print(word_list)
    elif action == "rev":
        for line in file1:
            print(line[::-1])
    elif action == "last":
        n = int(input("enter line number:"))
        for i in range(n):
            file1.readline()
        for line in file1:
            print(line)
    file1.close()


if __name__ == "__main__":
    main()
"""
