# 1. Function to create and return an empty list
def create_an_empty_list():
    return []  # Return an empty list

# 2. Function to create and return a list with some default elements
def create_a_list():
    return ["apple", "banana", "cherry", "date"]  # A list with 4 elements

# 3. Function to add an element to the end of the list
def add_element_to_end_of_list(l, element):
    l.append(element)  # Use append to add the element at the end
    return l  # Return the modified list

# 4. Function to add an element to the start of the list
def add_element_to_start_of_list(l, element):
    l.insert(0, element)  # Use insert to add the element at the start (index 0)
    return l  # Return the modified list

# 5. Function to remove the element from the end of the list
def remove_element_from_end_of_list(l):
    l.pop()  # Remove the last element
    return l  # Return the modified list

# 6. Function to remove the element from the start of the list
def remove_element_from_start_of_list(l):
    l.pop(0)  # Use pop(0) to remove and return the first element
    return l  # Return the modified list

# 7. Function to retrieve the first element from the list
def retrieve_first_element_from_list(l):
    return l[0]  # Access and return the first element (index 0)

# 8. Function to retrieve an element from a specific index
def retrieve_element_from_index(l, index):
    return l[index]  # Access and return the element at the specified index

# 9. Function to retrieve the last element from the list
def retrieve_last_element_from_list(l):
    return l[-1]  # Access and return the last element (index -1)
