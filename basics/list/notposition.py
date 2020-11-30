# Name: not_position
# Purpose: returns a list of the index positions that do not contain the element.
#          And we will use helper function to keep track of the position of the current element
# Precondition: The list can contain only integers.
#               Do not affect the list that is passed in and i should return a new list.
# Input Parameter(s):
#           my_list: a list containing only integers, and an element
# Return Value(s):
#           ---if the element is always in the list, return []
#           ---else the position of the list which don't contain the elemnet.
# Name: helper
#Purpose:It will take in a list and an element and the value count, and the initial value of count is zero,and returns a list of
#       numbers corresponding to the position that don't contain the element.
#Precondition: The list can contain only integers.
#               Do not affect the list that is passed in and i should return a new list.
#Input Parameters: it will take in a list, a element and count. the initial value of count is 0,
#                  use count to keep track of the position of mylist which don't contain the  element 
#Return Value: if the element is always in mylist, it will return an empty list
#              it the element is not in mylist, it will return the position of mylist which don't contain the element 

#============================================================================================
def not_position(mylist,element):
    return helper(mylist,element,0)

def helper(mylist,element,count):
    if mylist == []:
        return []
    elif mylist[0] != element:
        return [count]+helper(mylist[1:], element, count+1)
    else:
        return helper(mylist[1:], element, count +1)