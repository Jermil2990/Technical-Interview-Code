'''
Problem 4: Return Item

Implement a function get_item() that accepts a 0-indexed 
list items and a non-negative integer x and returns the 
element at index x in items. If x is not a valid index of items, 
return None.
'''
# Create a function get_item(), parameter list ( list, integer)
# Check if index is matches length of list if so print item at index    **len() get length of array
# If not return None

def get_item(items, x):
    if x < len(items):
        return items[x]
    else:
        return None

get_item(["pooh","rat","bird","Snake"], 2)