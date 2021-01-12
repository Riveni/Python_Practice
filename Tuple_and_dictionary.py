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
