# List is a data structure that allows us to combine multiple objects to one
empty_list = []
empty_list2 = list()

# List can hold different types of objects (int, float, strings and another lists)
multi_type_list = [5, 5.5, "star", ["list2"]]
list_of_letters = list("letters")  # [ 'l', 'e', 't', 't', 'e', 'r', 's' ]

# Accessing lists element
first_element = multi_type_list[0]
element_inside_list2 = multi_type_list[3][0]

# Assigning list elements to variables
a, b, c, d = multi_type_list

# Lists are mutable: it is possible to change, add or delete elements from it
empty_list.append("1")  # add element to the end of the list
empty_list[0] = "2"  # changing existing element
empty_list.remove("2")  # remove element by its name



