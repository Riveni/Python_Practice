# Tuple is a data structure that allows us to combine multiple objects to one
empty_tuple = ()
my_tuple = (5, "moon")
single_element_tuple = ("one",)
# Tuple is immutable! once tuple is defined the element inside it can not be modified
# Tuple is like read-only list that uses less memory space than list

# Tuples allows assignment of multiple variables at once and returning
# multiple values function
(food, food_type, calories) = ("bread", "whole wheat", 80)

# String formatting
basket_content = 3, "wine"
print("The basket contains %d bottles of %s." % basket_content)

# Dictionary is a data structure that holds values by theirs keys
empty_dict = {}
empty_dict2 = dict()
my_dict = {"key": "value", "key2": "value2"}

# Accessing dictionary values is done by using their key:
dict_value = my_dict["key"]

# Dictionary is mutable, and elements can be added, removed or modified
my_dict["new key"] = "new value"
my_dict["key"] = "modified value for existing key"
# Deletes element from the dictionary
del my_dict["key"]
my_dict.pop("key2")

# Dictionary view
my_dict.keys()
my_dict.values()
my_dict.items()

# Dictionary values can be mutable data types such as lists
# but dictionary keys must be immutable data type!
