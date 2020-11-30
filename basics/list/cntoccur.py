# Name: cnt_occur
# Purpose: return the numbers of times an interger on the list,
# count all of the int occurrences even if the int is embedded in inner lists.
# Precondition: The list can contain numerous data types
# (e.g. int, float, String, etc)
# Input Parameter(s):
#           my_list: a list containing numerous data types
# Return Value(s):
#           ---if there are no intergers, return 0
#           ---else return the numbers of intergers.
#============================================================================
def cnt_occur(mylist):
    if mylist == []:
        return 0
    elif type(mylist[0]) == int:
        return 1 + cnt_occur(mylist[1:])
    elif type(mylist[0]) == list:
        return cnt_occur(mylist[0]) + cnt_occur(mylist[1:])
    else:
        return cnt_occur(mylist[1:])