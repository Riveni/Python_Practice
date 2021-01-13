# Working with files
my_file = open("file_path", "mode") # mode can be "r" for read and "w" for write
""" modifying file"""
my_file.close()

# initial r tells python to ignore special chars like "\n" or "\t"
open_file = open(r"file_path", "mode")

# with statement allows us to work with files without explicitly close them
with open("file path", "mode") as my_file:
    """ work with file """

# Reading file content
# each line in the file is a string that ends with "\n"
file_content = my_file.read()  # copy all file content to the variable
file_content2 = my_file.readline()  # copy 1 line and move cursor to next line
file_content3 = my_file.readlines()  # copy all lines to list of strings
# using for loop:
for line in file_content:
    """each iteration it copy 1 line"""



