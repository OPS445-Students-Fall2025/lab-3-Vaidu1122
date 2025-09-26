#!/usr/bin/env python3

# AuthorID: 166249219
# Author: Vaidehi Patel

# Global list created here
my_list = [1, 2, 3, 4, 5]

def add_item_to_list(ordered_list):
    # Append the next integer (last element + 1) to the list
    next_value = ordered_list[-1] + 1
    ordered_list.append(next_value)

def remove_items_from_list(ordered_list, items_to_remove):
    # Remove all values, found in item_to_remove list, from ordered_list
    for item in items_to_remove:
        if item in ordered_list:
            ordered_list.remove(item)

# Main block
if __name__ == '__main__':
    print(my_list)                 # [1, 2, 3, 4, 5]
    add_item_to_list(my_list)      # [1, 2, 3, 4, 5, 6]
    add_item_to_list(my_list)      # [1, 2, 3, 4, 5, 6, 7]
    add_item_to_list(my_list)      # [1, 2, 3, 4, 5, 6, 7, 8]
    print(my_list)                 # [1, 2, 3, 4, 5, 6, 7, 8]
    remove_items_from_list(my_list, [1, 5, 6])
    print(my_list)                 # [2, 3, 4, 7, 8]

