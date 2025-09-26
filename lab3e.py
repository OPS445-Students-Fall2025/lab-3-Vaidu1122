#!/usr/bin/env python3

# AuthorID: 166249219
# Author: Vaidehi Patel

# declaring the list outside any function making it global object.
my_list = [100, 200, 300, 'six hundred']

#defining give_list() function
def give_list(): #Does not accept any argument 
    return my_list

#defining give_first_item() function
def give_first_item(): #Does not accept any argument
    #firstitem = my_list[0]
    return str(my_list[0])

#defining give_first_and_last_item() function
def give_first_and_last_item():
    #firstitem = my_list[0]
    #lastitem = my_list[-1]
    #newlist = [firstitem, lastitem]
    return [my_list[0], my_list[-1]]

#defining give_second_and_third_item() function
def give_second_and_third_item():
    #seconditem = my_list[1]
    #thirditem = my_list[2]
    #newlist = [seconditem, thirditem]
    return [my_list[1], my_list[2]]

#main block
if __name__ == "__main__":
    print(give_list())
    print(give_first_item())
    print(give_first_and_last_item())
    print(give_second_and_third_item())

