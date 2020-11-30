#Name: max_of_lists
#Purpose: Given a list which contains list of lists, which have numerical values,and then return the
#maximum value in a list of lists. 
#Precondition: The list contains lists, which have numerical values.
#Input Parameters(s)
#      my_list: a list contains lists, which have numerical value or the empty list.
#Return Value(s)
#        -- if the list that is passed in is the empty list, return a 0.
#        -- else find the maximum value of all the list in mylist, and then return the maximum value.
#====================================================================================
def max_of_lists(mylist):
    
    judge = False
    for i in mylist:
        for j in mylist[i]:
            judge = True
            if j > maximum:
                maximum = j
    if judge == False:
        return 0
    return maximum
